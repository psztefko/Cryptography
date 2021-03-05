import math

class CaesarCipher():

    ALPHABET_SIZE = 26
    SMALL_A_ASCII_CODE = 97
    ENGLISH_LETTER_PROBABILITIES = [
		0.08167, 0.01492, 0.02782, 0.04253, 0.12702, 0.02228, 0.02015, 0.06094, 0.06966, 0.00153, 0.00772, 0.04025, 0.02406,
		0.06749, 0.07507, 0.01929, 0.00095, 0.05987, 0.06327, 0.09056, 0.02758, 0.00978, 0.02360, 0.00150, 0.01974, 0.00074];

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

    # Calculating entropy of given string
    def calculateEntropy(self, string: str) -> float:
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
    def automateHack(self, dictOfPossibilities) -> str:
        entropy = float('inf')
        righKey = -1
        for key, value in dictOfPossibilities.items():
            currentEntropy = self.calculateEntropy(value)
            if currentEntropy < entropy:
                entropy = currentEntropy
                righKey = key


        return dictOfPossibilities[righKey]