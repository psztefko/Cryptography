import logging
from string import ascii_lowercase, punctuation
import random

ENGLISH_LETTER_PROBABILITIES = {
		"a":0.08167, "b":0.01492, "c":0.02782, "d":0.04253, "e":0.12702, "f":0.02228, "g":0.02015, "h":0.06094, "i":0.06966, "j":0.00153, "k":0.00772, "l":0.04025, "m":0.02406,
		"n":0.06749, "o":0.07507, "p":0.01929, "q":0.00095, "r":0.05987, "s":0.06327, "t":0.09056, "u":0.02758, "v":0.00978, "w":0.02360, "x":0.00150, "y":0.01974, "z":0.00074}


class Decrypt():

    logger = logging.getLogger('decrypt')
    logging.basicConfig(level=logging.DEBUG)

    def __init__(self, cipherText: str):
        self.cipherText = cipherText

    def __count_frequency(self):
        """Creates dictionary of chars with frequency of their occurrences"""

        charsFreq = {char: 0 for char in ascii_lowercase}

        for char in self.cipherText:
            if char != " " and char in charsFreq:
                charsFreq[char] += 1

        self.logger.info("Counted character frequency")

        return charsFreq


    def __decrypt_spaces(self, text):
        """Decrypts all spaces"""

        output = ""

        index = 0
        while index < len(text):

            if text[index] in punctuation:
                if text[index + 1] in ascii_lowercase:
                    if text[index + 2] in punctuation:
                        output += " "
                        index += 2
            else:
                output += text[index]

            index += 1

        self.cipherText = output
        self.logger.info("Decrypted spaces in text")


    def __decrypt_monoalphabetic(self) -> str:
        """Decrypts monoalphabetic cipher"""

        plainText = ""

        sortedEnglishLetterProbabilities = list(
            dict(sorted(ENGLISH_LETTER_PROBABILITIES.items(), key=lambda item: item[1], reverse=True)).keys())
        reversedEnglishLetterProbabilities = list(
            dict(sorted(ENGLISH_LETTER_PROBABILITIES.items(), key=lambda item: item[1], reverse=False)).keys())

        dictOfCombinedChars = dict(zip(reversedEnglishLetterProbabilities, sortedEnglishLetterProbabilities))

        for char in self.cipherText:
            if char != " ":
                plainText += dictOfCombinedChars[char]
            else:
                plainText += " "


        self.cipherText = plainText
        self.logger.info("Decrypted monoalphabetic cipher")


    def __remove_spaces(self):
        """"Removes all spaces from ciphertext"""

        self.cipherText = self.cipherText.replace(" ", "")

    def decrypt(self):
        """Decrypts ciphertext"""

        self.__remove_spaces()
        self.__decrypt_spaces(self.cipherText)
        self.__decrypt_monoalphabetic()

        return self.cipherText