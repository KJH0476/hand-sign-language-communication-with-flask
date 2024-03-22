from service.label import Label

L = Label()

temp_store=[]
temp = 0
last_chosung_index = None
last_jungsung_index = None
last_jungsung_text = None

combined_vowel_map = {
    ('ㅗ', 'ㅏ'): 'ㅘ',
    ('ㅗ', 'ㅐ'): 'ㅙ',
    ('ㅜ', 'ㅓ'): 'ㅝ',
    ('ㅜ', 'ㅔ'): 'ㅞ'
}

#text: 자음 or 모음 값, sta: 초성(0), 중성(1), 종성(2), 단어(3), 숫자(4) 구분
def make_text(text, sta):
    global temp_store, temp, last_chosung_index, last_jungsung_index, last_jungsung_text
    imp_text='' #임시 리턴 텍스트

    # 초성, 중성, 종성 인덱스 찾기
    if sta==0:
        chosung_index = L.consonant_map.get(text, 0)
        # 이전 초성과 동일한 경우 더블 초성 처리
        if chosung_index == last_chosung_index:
            #쌍자음으로 변환 (예: 'ㅂ' -> 'ㅃ')
            last_chosung_index = chosung_index + 1
            temp = 0xAC00 + (last_chosung_index * 21 * 28)
        else:
            temp = 0xAC00 + (chosung_index * 21 * 28)
            last_chosung_index = chosung_index

        print(chr(temp))
        last_jungsung_index = None
        imp_text = chr(temp)  # '아'로 초기화 전에 저장
    elif sta==1:
        jungsung_index = L.vowel_map.get(text, 0)
        if jungsung_index == 8: last_jungsung_index = jungsung_index
        elif jungsung_index == 13: last_jungsung_index = jungsung_index
        else:
            if last_jungsung_index == 8:
                jungsung_index = last_jungsung_index + jungsung_index + 1
                temp_store[-1] = chr(0xAC00 + (last_chosung_index * 21 * 28) + (jungsung_index * 28))
                imp_text = chr(temp)
                temp = 50500
                last_chosung_index = None
                return imp_text
            elif last_jungsung_index == 13:
                jungsung_index = last_jungsung_index + jungsung_index - 3
                temp_store[-1] = chr(0xAC00 + (last_chosung_index * 21 * 28) + (jungsung_index * 28))
                imp_text = chr(temp)
                temp = 50500
                last_chosung_index = None
                return imp_text
            last_chosung_index = None
        temp += (jungsung_index * 28)
        temp_store.append(chr(temp))
        imp_text = chr(temp)
        temp = 50500
        print(chr(temp))
    elif sta==2:
        jongsung_index = L.final_consonant_map.get(text, 0)
        if jongsung_index!=0:
            temp_store[-1] = chr(ord(temp_store[-1]) + jongsung_index)
            imp_text = temp_store[-1]  # '아'로 초기화 전에 저장
        last_chosung_index = None; last_jungsung_index = None
    elif sta==3 or sta==4:
        temp_store.append(text)
        imp_text = chr(temp)  # '아'로 초기화 전에 저장
        temp = 50500 #temp 초기화
        last_chosung_index = None; last_jungsung_index = None
    return imp_text

def clear_hangul_store():
    temp_store.clear()
