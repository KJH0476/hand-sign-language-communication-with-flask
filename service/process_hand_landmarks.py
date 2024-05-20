import numpy as np

def process_hand_landmarks(hand_landmarks, landmark_indices, model,label_dict):
    data_aux = []
    x_ = []
    y_ = []
    for lm_idx in landmark_indices:
        lm = hand_landmarks.landmark[lm_idx]
        x_.append(lm.x)
        y_.append(lm.y)

    min_x = min(x_)
    min_y = min(y_)

    for lm_idx in landmark_indices:
        lm = hand_landmarks.landmark[lm_idx]
        data_aux.append(lm.x - min_x)
        data_aux.append(lm.y - min_y)

    prediction = model.predict([np.asarray(data_aux)])
    recognized_text = label_dict[prediction[0]]

    return recognized_text