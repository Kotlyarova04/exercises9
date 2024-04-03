cclass MorseMsg:
    MORSE_CODE_DICT = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
        'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
        'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
        'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..',
        'А': '.-', 'Б': '-...', 'В': '.--', 'Г': '--.', 'Д': '-..', 'Е': '.',
        'Ё': '.', 'Ж': '...-', 'З': '--..', 'И': '..', 'Й': '.---', 'К': '-.-',
        'Л': '.-..', 'М': '--', 'Н': '-.', 'О': '---', 'П': '.--.', 'Р': '.-.',
        'С': '...', 'Т': '-', 'У': '..-', 'Ф': '..-.', 'Х': '....', 'Ц': '-.-.',
        'Ч': '---.', 'Ш': '----', 'Щ': '--.-', 'Ъ': '--.--', 'Ы': '-.--',
        'Ь': '-..-', 'Э': '..-..', 'Ю': '..--', 'Я': '.-.-'
    }

    def __init__(self, morse_code):
        self.morse_code = morse_code.split()

    def eng_decode(self):
        decoded = ''
        for symbol in self.morse_code:
            decoded += list(self.MORSE_CODE_DICT.keys())[list(self.MORSE_CODE_DICT.values()).index(symbol)]
        return decoded

    def ru_decode(self):
        decoded = ''
        for symbol in self.morse_code:
            decoded += list(self.MORSE_CODE_DICT.keys())[list(self.MORSE_CODE_DICT.values()).index(symbol)]
        return decoded

    def get_vowels(self, lang):
        vowels_eng = 'AEIOU'
        vowels_ru = 'АЕИОУЫЭЮЯ'
        decoded = self.eng_decode() if lang == 'eng' else self.ru_decode()
        return [letter for letter in decoded if letter in (vowels_eng if lang == 'eng' else vowels_ru)]

    def get_consonants(self, lang):
        consonants_eng = 'BCDFGHJKLMNPQRSTVWXYZ'
        consonants_ru = 'БВГДЖЗЙКЛМНПРСТФХЦЧШЩЬЪ'
        decoded = self.eng_decode() if lang == 'eng' else self.ru_decode()
        return [letter for letter in decoded if letter in (consonants_eng if lang == 'eng' else consonants_ru