import variable
from service import make_hangul, chatgpt_make_answer, separate_hangul

store = []

def store_recognition_data(character, coordinates):
    if character in variable.recognition_data:
        variable.recognition_data[character][0] += 1
        variable.recognition_data[character][1] = coordinates
    else:
        variable.recognition_data[character] = [1, coordinates]

    print(f"data: {character}, {variable.recognition_data[character][1]}")

    #10번 인식되면 확정 처리
    if variable.recognition_data[character][0] >= 10:
        #초성
        if (variable.recognition_data[character][1][0] <= variable.square_center_x and variable.recognition_data[character][1][1] <= variable.square_center_y)\
                or (variable.square_center_x-130 <= variable.recognition_data[character][1][0] <= variable.square_center_x and variable.recognition_data[character][1][1] <= variable.square_center_y): sta = 0
        #중성
        elif variable.recognition_data[character][1][0] > variable.square_center_x and variable.recognition_data[character][1][1] <=variable.square_center_y: sta = 1
        #종성
        elif variable.recognition_data[character][1][1] > variable.square_center_y: sta = 2
        # 단어
        else: sta = 3

        #숫자
        if character.isdigit() or (character=='ㅏ' and (sta==0 or sta==2)) or (character=='ㅑ' and (sta==0 or sta==2)):
            if character == 'ㅏ': character = '1'
            elif character == 'ㅑ': character = '2'
            sta = 4

        #딕셔너리 초기화
        variable.recognition_data.clear()
        confirm_recognition_data(character, sta)

def confirm_recognition_data(character, sta):
    global store
    store.append(character)
    print(f"Confirmed recognition data: {character}, {sta}")
    print(store)
    text = make_hangul.make_text(character, sta)
    print(text, sta, make_hangul.temp_store)
    variable.socketio.emit('flash_border', {'status': 'confirmed', 'text': text})

    #전송 동작을 하면 지피티에게 완성된 문장 요청 보냄
    if character=='전송':
        gpt_prompt = ''.join(make_hangul.temp_store)
        make_hangul.temp_store.clear()
        gpt_answer = chatgpt_make_answer.request_gpt_answer(gpt_prompt)
        print(gpt_answer)

        #받응 응답을 분리
        separate_text = separate_hangul.separate_text(gpt_answer)
        print(separate_text)

        #분리된 텍스트를 언리얼 클라이언트에게 소켓 전송
        #socketio.emit('answer', separate_text)