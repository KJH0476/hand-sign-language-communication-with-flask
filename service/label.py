class Label:
    labels_dict = None
    labels_dict_digut = None

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
            '31_Left': '3', '31_Right': '3',
            '32_Left': '4', '32_Right': '4',
            '33_Left': '5', '33_Right': '5',
            '34_Left': '6', '34_Right': '6',
            '35_Left': '7', '35_Right': '7',
            '36_Left': '8', '36_Right': '8',
            '37_Left': '9', '37_Right': '9',
            '38_Left': '전송', '38_Right': '전송'
        }
        
        # 모델별 라벨
        labels_dict_digut = {
        '0_Left': 'ㄷ', '1_Left': 'ㄹ', '2_Left': 'ㅌ', 
        '0_Right': 'ㄷ', '1_Right': 'ㄹ', '2_Right': 'ㅌ'
        }
        labels_dict_siot = {'0_Left': 'ㅅ', '1_Left': 'ㅠ', '2_Left': 'ㅈ','3_Left': 'ㅊ','4_Left': 'ㅋ', 
               '0_Right': 'ㅅ', '1_Right': 'ㅠ', '2_Right': 'ㅈ', '3_Right': 'ㅊ', '4_Right': 'ㅋ'}
        labels_dict_ye = {'0_Left': 'ㅓ', '1_Left': 'ㅕ', '2_Left': 'ㅔ','3_Left': 'ㅖ', 
               '0_Right': 'ㅓ', '1_Right': 'ㅕ', '2_Right': 'ㅔ', '3_Right': 'ㅖ'}
        
        # 모델 라벨 초기화
        self.labels_dict = labels_dict
        self.labels_dict_digut = labels_dict_digut
        self.labels_dict_siot = labels_dict_siot
        self.labels_dict_ye = labels_dict_ye
        # 초성 맵 초기화
        consonants = ["ㄱ", "ㄲ", "ㄴ", "ㄷ", "ㄸ", "ㄹ", "ㅁ", "ㅂ", "ㅃ", "ㅅ", "ㅆ", "ㅇ", "ㅈ", "ㅉ", "ㅊ", "ㅋ", "ㅌ", "ㅍ", "ㅎ"]
        self.consonant_map = {consonant: i for i, consonant in enumerate(consonants)}

        # 중성 맵 초기화
        vowels = ["ㅏ", "ㅐ", "ㅑ", "ㅒ", "ㅓ", "ㅔ", "ㅕ", "ㅖ", "ㅗ", "ㅘ", "ㅙ", "ㅚ", "ㅛ", "ㅜ", "ㅝ", "ㅞ", "ㅟ", "ㅠ", "ㅡ", "ㅢ", "ㅣ"]
        self.vowel_map = {vowel: i for i, vowel in enumerate(vowels)}

        # 종성 맵 초기화
        final_consonants = [" ", "ㄱ", "ㄲ", "ㄳ", "ㄴ", "ㄵ", "ㄶ", "ㄷ", "ㄹ", "ㄺ", "ㄻ", "ㄼ", "ㄽ", "ㄾ", "ㄿ", "ㅀ", "ㅁ", "ㅂ", "ㅄ", "ㅅ", "ㅆ", "ㅇ", "ㅈ", "ㅊ", "ㅋ", "ㅌ", "ㅍ", "ㅎ"]
        self.final_consonant_map = {final_consonant: i for i, final_consonant in enumerate(final_consonants)}