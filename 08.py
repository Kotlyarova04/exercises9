class MorseMsg:
    MORSE_CODE_ENG = {
        'A': '.-', 'B': '-...',
        'C': '-.-.', 'D': '-..',
        'E': '.', 'F': '..-.',
        'G': '--.', 'H': '....',
        'I': '..', 'J': '.---',
        'K': '-.-', 'L': '.-..',
        'M': '--', 'N': '-.',
        'O': '---', 'P': '.--.',
        'Q': '--.-', 'R': '.-.',
        'S': '...', 'T': '-',
        'U': '..-', 'V': '...-',
        'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..',}
    MORSE_CODE_RU = {
        'А': '.-', 'Б': '-...',
        'В': '.--', 'Г': '--.',
        'Д': '-..', 'Е': '.',
        'Ё': '.', 'Ж': '...-',
        'З': '--..', 'И': '..',
        'Й': '.---', 'К': '-.-',
        'Л': '.-..', 'М': '--',
        'Н': '-.', 'О': '---',
        'П': '.--.', 'Р': '.-.',
        'С': '...', 'Т': '-',
        'У': '..-', 'Ф': '..-.',
        'Х': '....', 'Ц': '-.-.',
        'Ч': '---.', 'Ш': '----',
        'Щ': '--.-', 'Ъ': '--.--',
        'Ы': '-.--','Ь': '-..-',
        'Э': '..-..', 'Ю': '..--',
        'Я': '.-.-'}


    def __init__(self, morse):
        self.morse = morse.split()
        print(self.morse)

    def eng_decode(self):
        decode = ''
        for symbol in self.morse:
            decode += list(self.MORSE_CODE_ENG.keys())[list(self.MORSE_CODE_ENG.values()).index(symbol)]
        return decode

    def ru_decode(self):
        decode = ''
        for symbol in self.morse:
            decode += list(self.MORSE_CODE_RU.keys())[list(self.MORSE_CODE_RU.values()).index(symbol)]
        return decode

    def get_vowels(self, lang):
        vowels_eng = 'AEIOU'
        vowels_ru = 'АЕИОУЫЭЮЯ'
        vowels = []
        if lang == 'eng':
            decode = self.eng_decode()
        else:
            decode = self.ru_decode()
        if lang == 'eng':
            for letter in decode:
                if letter in vowels_eng:
                    vowels.append(letter)
        else:
            for letter in decode:
                if letter in vowels_ru:
                    vowels.append(letter)
        return vowels

    def get_consonants(self, lang):
        consonants_eng = 'BCDFGHJKLMNPQRSTVWXYZ'
        consonants_ru = 'БВГДЖЗЙКЛМНПРСТФХЦЧШЩЬЪ'
        consonants = []
        if lang == 'eng':
            decode = self.eng_decode()
        else:
            decode = self.ru_decode()
        if lang == 'eng':
            for letter in decode:
                if letter in consonants_eng:
                    consonants.append(letter)
        else:
            for letter in decode:
                if letter in consonants_ru:
                    consonants.append(letter)
        return consonants


morse_msg = MorseMsg('.- -... .--')
print(morse_msg.ru_decode())
print(morse_msg.get_vowels('ru'))
