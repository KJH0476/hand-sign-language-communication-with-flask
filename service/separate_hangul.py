from service.label import Label

def separate_text(text):

    #유니코드 한글 시작과 끝 지점
    BASE_CODE, CHOSUNG, JUNGSUNG = 44032, 588, 28

    result = list()

    words = text.split()
    for word in words:
        if word in Label.WORD_LIST:  #단어인 경우 그대로 추가
            result.append((word, 3))
        else:  #단어가 아닌 경우 분리
            for char in word:
                if ord('가') <= ord(char) <= ord('힣'):  #한글 문자인 경우
                    char_code = ord(char) - BASE_CODE
                    char1 = char_code // CHOSUNG
                    char2 = ((char_code - (CHOSUNG * char1)) // JUNGSUNG)
                    char3 = (char_code - (CHOSUNG * char1) - (JUNGSUNG * char2))
                    result.append((Label.CHOSUNG_LIST[char1], 0))  #초성
                    result.append((Label.JUNGSUNG_LIST[char2], 1))  #중성
                    if char3 > 0:   #받침이 있는 경우
                        result.append((Label.JONGSUNG_LIST[char3], 2))  #종성
                elif char in Label.NUMBER_LIST:  #숫자인 경우
                    result.append((int(char), 4))
                else:  # 한글이 아닌 경우(특수 문자)
                    result.append((char, -1))

    return result
