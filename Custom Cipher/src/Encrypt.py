import logging
from string import ascii_lowercase, punctuation
import random
import numpy

ENGLISH_LETTER_PROBABILITIES = {
    "a": 0.08167, "b": 0.01492, "c": 0.02782, "d": 0.04253, "e": 0.12702, "f": 0.02228, "g": 0.02015, "h": 0.06094,
    "i": 0.06966, "j": 0.00153, "k": 0.00772, "l": 0.04025, "m": 0.02406,
    "n": 0.06749, "o": 0.07507, "p": 0.01929, "q": 0.00095, "r": 0.05987, "s": 0.06327, "t": 0.09056, "u": 0.02758,
    "v": 0.00978, "w": 0.02360, "x": 0.00150, "y": 0.01974, "z": 0.00074}


class Encrypt:
    logger = logging.getLogger('encrypt')
    logging.basicConfig(level=logging.DEBUG)

    def __init__(self, plainText: str):
        self.plainText = ''

        # removes from plaintext everything except of alphanumeric and spaces
        for char in plainText:
            if char.isalpha() or char == ' ':
                self.plainText += char.lower()

        self.prefix = None

    def __encrypt_spaces(self):
        """Replaces every space in text with randomly generated characters"""

        self.plainText = self.plainText.replace(' ', ''.join(
            [random.choice(punctuation)] + [random.choice(ascii_lowercase)] + [random.choice(punctuation)]))
        self.logger.info('Encrypted every spaces in text')

    def __monoalphabetic(self):
        """Swaps letters from plaintext with high occurency to less frequent used ones"""

        ciphertext = ''

        sortedEnglishLetterProbabilities = list(
            dict(sorted(ENGLISH_LETTER_PROBABILITIES.items(), key=lambda item: item[1], reverse=True)).keys())
        reversedEnglishLetterProbabilities = list(
            dict(sorted(ENGLISH_LETTER_PROBABILITIES.items(), key=lambda item: item[1], reverse=False)).keys())

        dictOfCombinedChars = dict(zip(sortedEnglishLetterProbabilities, reversedEnglishLetterProbabilities))

        for char in self.plainText:
            if char != ' ':
                ciphertext += dictOfCombinedChars[char]
            else:
                ciphertext += ' '

        self.plainText = ciphertext
        self.logger.info('Encrypted text using monoalphabetic cipher')

    def __insert_random_spaces(self):
        """Inserts spaces randomly to mislead code breaker"""

        output = ''
        index = 0

        while index < len(self.plainText):
            # generates the length between spaces using the word length distribution in English language
            shift = numpy.random.choice(numpy.arange(3, 11), p=[0.07, 0.1, 0.14, 0.16, 0.16, 0.15, 0.12, 0.1])

            if index + shift < len(self.plainText):
                for i in range(shift):
                    output += self.plainText[index + i]

                output += ' '
            else:
                for i in range(len(self.plainText) - index):
                    output += self.plainText[index + i]

            index += shift

        self.plainText = output
        self.logger.info('Misleading spaces added to ciphertext')

    def __transpose_text(self):
        """Transposes text"""

        key = random.randint(10, 36)
        transposedText = [''] * key

        for column in range(key):
            pointer = column

            while pointer < len(self.plainText):
                transposedText[column] += self.plainText[pointer]
                pointer += key

        self.plainText = ''.join(transposedText)
        self.prefix = ascii_lowercase[key - 11]
        self.logger.info('Transposed text')

    def encrypt(self) -> str:
        """Encrypts message using other methods"""

        self.__monoalphabetic()
        self.__encrypt_spaces()
        self.__transpose_text()
        self.plainText = self.prefix + self.plainText
        self.__insert_random_spaces()

        self.logger.info('Message successfully encrypted')

        return self.plainText
