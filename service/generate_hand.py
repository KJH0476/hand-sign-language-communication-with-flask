import cv2
import time
import mediapipe as mp
import numpy as np
import variable
from service.label import Label
import service.process_hand_landmarks as P
from utilities import drawing, reconized_hand

cap = None
frame = None

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

hands = mp_hands.Hands(static_image_mode=False, max_num_hands=2, min_detection_confidence=0.5,
                       min_tracking_confidence=0.5)

# 윈도우 폰트
font_path = 'C:/Windows/Fonts/malgun.ttf'

## 맥북 폰트
#font_path = '/Library/Fonts/AppleGothic.ttf'

L = Label()

def generate_frames(model, model_digut,model_siot,model_ye):
    global cap, frame
    last_time = time.time()
    box_index = 0
    last_recognition_update = time.time()
    recognition_interval = 0.2  # 인식 업데이트 간격 (0.2초)
    
    prev_landmarks = None  # 이전 프레임의 랜드마크 값 저장을 위한 변수 (동적, 정적 판별)
    
    if cap is None or not cap.isOpened():
        cap = cv2.VideoCapture(0)  # 기본 카메라로 대체 시도
        if not cap.isOpened():
            raise ValueError("Unable to open video source")

    while True:
        success, frame = cap.read()
        if not success:
            print("Frame read error!!!")
            continue

        frame = cv2.resize(frame, (1300, 800))
        H, W, _ = frame.shape
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(frame_rgb)

        drawing.draw_box(frame)

        if results.multi_hand_landmarks:
            for hand_index, hand_landmarks in enumerate(results.multi_hand_landmarks):
                data_aux = []
                x_ = []
                y_ = []
                
                current_landmarks = []  # 현재 프레임의 랜드마크 값을 저장할 리스트 (동적, 정적 판별)
                
                # 원하는 랜드마크의 인덱스 지정 
                digut_index = [6, 7, 8, 10, 11, 12, 14, 15, 16]
                siot_index = [2,3,4,6,7,8,10,11,12,14,15,16]
                ye_index =  [6,7,8,10,11,12,14,15,16,18,19,20]
                
                for lm in hand_landmarks.landmark:
                    x, y = lm.x, lm.y
                    x_.append(x)
                    y_.append(y)

                min_x = min(x_)
                min_y = min(y_)

                for lm in hand_landmarks.landmark:
                    data_aux.append(lm.x - min_x)
                    data_aux.append(lm.y - min_y)
                    current_landmarks.append((lm.x, lm.y))  # 현재 landmark값 추출
                    
                if prev_landmarks is not None:
                    # 이전 프레임과 현재 프레임의 랜드마크 값 간의 유클리드 거리 계산
                    landmark_distance = np.linalg.norm(np.array(prev_landmarks) - np.array(current_landmarks))
                    threshold = 0.2  # 임의로 선택한 임계값 - 조정 필요
                    if landmark_distance > threshold:
                        # 여기에 flag 같은거 설정해서 동적 정적 판별할 수 있는 변수 추가
                        print("움직임이 감지되었습니다!")
                        
                prev_landmarks = current_landmarks  # 현재 프레임의 랜드마크 값을 이전 프레임 변수에 저장

                prediction = model.predict([np.asarray(data_aux)])
                recognized_text = L.labels_dict[prediction[0]]
                
                 # 특정 라벨 처리
                if recognized_text in ['ㄷ', 'ㄹ', 'ㅌ']:
                        recognized_text = P.process_hand_landmarks(hand_landmarks, digut_index, model_digut,L.labels_dict_digut)
                elif recognized_text in ['ㅅ', 'ㅠ', 'ㅈ', 'ㅊ', 'ㅋ']:
                        recognized_text = P.process_hand_landmarks(hand_landmarks, siot_index, model_siot,L.labels_dict_siot)
                elif recognized_text in ['ㅓ', 'ㅕ', 'ㅖ', 'ㅔ']:
                        recognized_text = P.process_hand_landmarks(hand_landmarks, ye_index, model_ye,L.labels_dict_ye)
                    
                x1 = int(min(x_) * W) - 10
                y1 = int(min(y_) * H) - 10
                recognized_coordinates = (x1, y1)

                # 박스의 중심점 좌표 계산
                center_x = int((min(x_) + max(x_)) * W / 2)
                center_y = int((min(y_) + max(y_)) * H / 2)
                recognized_coordinates_center = (center_x, center_y)

                #print(f"단어: {recognized_text}, 좌표: {recognized_coordinates_center}")

                # 인식된 문자와 좌표를 화면에 그림
                frame = drawing.draw_hangul_text(frame, recognized_text, (recognized_coordinates[0], recognized_coordinates[1] - 70), font_path, 50, (0, 0, 0))
                cv2.putText(frame, f"{recognized_coordinates_center}", (recognized_coordinates_center[0] + 10, recognized_coordinates_center[1]), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
                cv2.circle(frame, recognized_coordinates_center, 10, (255, 255, 0), -1)

                # 각 프레임마다 손 랜드마크를 그림.
                #mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS, mp_drawing_styles.get_default_hand_landmarks_style(), mp_drawing_styles.get_default_hand_connections_style())
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                if time.time() - last_recognition_update > recognition_interval:
                    #좌표 값이 범위 안에 들어왔을 때만 인식
                    if (variable.square_center_x-130 <= center_x <= variable.square_center_x+130
                            and variable.square_center_y-210 <= center_y <= variable.square_center_y+210)\
                            or (variable.square_center_x-130 <= center_x <= variable.square_center_x+130
                            and variable.square_center_y-210 <= center_y <= variable.square_center_y+210):
                        reconized_hand.store_recognition_data(recognized_text, (center_x, center_y))
                    #단어일 경우 범위 밖에서도 인식
                    else:
                        if len(variable.recognition_data) > 1: reconized_hand.store_recognition_data(recognized_text, (-1,-1));
                    last_recognition_update = time.time()

        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')