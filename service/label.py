class Label:
    labels_dict = None

    # 초성, 중성, 종성, 단어, 숫자 리스트
    CHOSUNG_LIST = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
    JUNGSUNG_LIST = ['ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ', 'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ',
                     'ㅣ']
    JONGSUNG_LIST = ['', 'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ',
                     'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
    WORD_LIST = ['안녕하세요', '나는', '바보', '안녕!', '반가워']
    NUMBER_LIST = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    def __init__(self):
        #라벨 데이터
        # labels_dict 수정
        labels_dict = {
            '0_Left': 'ㄱ', '0_Right': 'ㄱ',
            '1_Left': 'ㄴ', '1_Right': 'ㄴ',
            '2_Left': 'ㄷ', '2_Right': 'ㄷ',
            '3_Left': 'ㄹ', '3_Right': 'ㄹ',
            '4_Left': 'ㅁ', '4_Right': 'ㅁ',
            '5_Left': 'ㅂ', '5_Right': 'ㅂ',
            '6_Left': 'ㅅ', '6_Right': 'ㅅ',
            '7_Left': 'ㅇ', '7_Right': 'ㅇ',
            '8_Left': 'ㅈ', '8_Right': 'ㅈ',
            '9_Left': 'ㅊ', '9_Right': 'ㅊ',
            '10_Left': 'ㅋ', '10_Right': 'ㅋ',
            '11_Left': 'ㅌ', '11_Right': 'ㅌ',
            '12_Left': 'ㅍ', '12_Right': 'ㅍ',
            '13_Left': 'ㅎ', '13_Right': 'ㅎ',
            '14_Left': 'ㅏ', '14_Right': 'ㅏ',
            '15_Left': 'ㅐ', '15_Right': 'ㅐ',
            '16_Left': 'ㅑ', '16_Right': 'ㅑ',
            '17_Left': 'ㅒ', '17_Right': 'ㅒ',
            '18_Left': 'ㅓ', '18_Right': 'ㅓ',
            '19_Left': 'ㅔ', '19_Right': 'ㅔ',
            '20_Left': 'ㅕ', '20_Right': 'ㅕ',
            '21_Left': 'ㅖ', '21_Right': 'ㅖ',
            '22_Left': 'ㅗ', '22_Right': 'ㅗ',
            '23_Left': 'ㅛ', '23_Right': 'ㅛ',
            '24_Left': 'ㅜ', '24_Right': 'ㅜ',
            '25_Left': 'ㅠ', '25_Right': 'ㅠ',
            '26_Left': 'ㅡ', '26_Right': 'ㅡ',
            '27_Left': 'ㅣ', '27_Right': 'ㅣ',
            '28_Left': 'ㅚ', '28_Right': 'ㅚ',
            '29_Left': 'ㅟ', '29_Right': 'ㅟ',
            '30_Left': 'ㅢ', '30_Right': 'ㅢ',
            '31_Left': '0', '31_Right': '0',
            '32_Left': '1', '32_Right': '1',
            '33_Left': '2', '33_Right': '2',
            '34_Left': '3', '34_Right': '3',
            '35_Left': '4', '35_Right': '4',
            '36_Left': '5', '36_Right': '5',
            '37_Left': '6', '37_Right': '6',
            '38_Left': '7', '38_Right': '7',
            '39_Left': '8', '39_Right': '8',
            '40_Left': '9', '40_Right': '9'
            # ,'41_Left': 'unknown', '41_Right': 'unknown'
        }

        self.labels_dict = labels_dict

        # 초성 맵 초기화
        consonants = ["ㄱ", "ㄲ", "ㄴ", "ㄷ", "ㄸ", "ㄹ", "ㅁ", "ㅂ", "ㅃ", "ㅅ", "ㅆ", "ㅇ", "ㅈ", "ㅉ", "ㅊ", "ㅋ", "ㅌ", "ㅍ", "ㅎ"]
        self.consonant_map = {consonant: i for i, consonant in enumerate(consonants)}

        # 중성 맵 초기화
        vowels = ["ㅏ", "ㅐ", "ㅑ", "ㅒ", "ㅓ", "ㅔ", "ㅕ", "ㅖ", "ㅗ", "ㅘ", "ㅙ", "ㅚ", "ㅛ", "ㅜ", "ㅝ", "ㅞ", "ㅟ", "ㅠ", "ㅡ", "ㅢ", "ㅣ"]
        self.vowel_map = {vowel: i for i, vowel in enumerate(vowels)}

        # 종성 맵 초기화
        final_consonants = [" ", "ㄱ", "ㄲ", "ㄳ", "ㄴ", "ㄵ", "ㄶ", "ㄷ", "ㄹ", "ㄺ", "ㄻ", "ㄼ", "ㄽ", "ㄾ", "ㄿ", "ㅀ", "ㅁ", "ㅂ", "ㅄ", "ㅅ", "ㅆ", "ㅇ", "ㅈ", "ㅊ", "ㅋ", "ㅌ", "ㅍ", "ㅎ"]
        self.final_consonant_map = {final_consonant: i for i, final_consonant in enumerate(final_consonants)}