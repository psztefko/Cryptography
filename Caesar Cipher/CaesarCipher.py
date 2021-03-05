import math

class CaesarCipher():

    ALPHABET_SIZE = 26
    SMALL_A_ASCII_CODE = 97
    ENGLISH_LETTER_PROBABILITIES = [0.073, 0.009, 0.030, 0.044, 0.130, 0.028, 0.016, 0.035, 0.074,
                                    0.002, 0.003, 0.035, 0.025, 0.078, 0.074, 0.027, 0.003,
                                    0.077, 0.063, 0.093, 0.027, 0.013, 0.016, 0.005, 0.019, 0.001]

    # Encrypts plain text using given key
    def encrypt(self, string: str, key: int) -> str:
        cipher = ''

        # iterate through every character in plain text
        for i in range(len(string)):
            char = string[i].lower()
            # checks whether character is alphanumeric or space and encrypts it
            if char.isspace():
                cipher += ' '
            elif char.isalpha():
                cipher += chr((ord(char) + key - self.SMALL_A_ASCII_CODE) % self.ALPHABET_SIZE + self.SMALL_A_ASCII_CODE)
        return cipher

    # Decrypts encrypted text using given key
    def decrypt(self, string: str, key: int) -> str:
        return self.encrypt(string, -key)

    # Creates dictionary with every possibility of key
    def createDictionaryOfPossibilities(self, string: str) -> str:
        dictionaryOfGuesses = {}

        for i in range(26):
            plainText = ''
            for char in string:
                if (char.isspace()):
                    plainText += ' '
                else:
                    plainText += chr((ord(char) - i - self.SMALL_A_ASCII_CODE) % self.ALPHABET_SIZE + self.SMALL_A_ASCII_CODE)

            dictionaryOfGuesses[i + 1] = plainText
        return dictionaryOfGuesses

    # Creates dictionary with every possibility of key
    def createDictionaryOfPossibilities(self, string: str) -> str:
        dictionaryOfGuesses = {}

        for i in range(26):
            plainText = ''
            for char in string:
                if (char.isspace()):
                    plainText += ' '
                else:
                    plainText += chr((ord(char) - i - self.SMALL_A_ASCII_CODE) % self.ALPHABET_SIZE + self.SMALL_A_ASCII_CODE)

            dictionaryOfGuesses[i + 1] = plainText
        return dictionaryOfGuesses


    def calculateEntropy(self, string: str):
        sum = 0
        spaces = 0

        for char in string:
            asciiCode = ord(char)
            if char.isspace():
                spaces += 1
            else:
                sum += math.log(self.ENGLISH_LETTER_PROBABILITIES[asciiCode - self.SMALL_A_ASCII_CODE])

        return -sum / math.log(2) / (len(string) - spaces)

    # Automatically cracks key by comparing entropy of every possibility (string with lowest entropy is most probably correct answer)
    def automateHack(self, dictOfPossibilities):
        entropy = float('inf')
        righKey = -1
        for key, value in dictOfPossibilities.items():
            currentEntropy = self.calculateEntropy(self.decrypt(value, key + 1))
            if currentEntropy < entropy:
                entropy = currentEntropy
                righKey = key


        return dictOfPossibilities[righKey]
