import logging
from string import ascii_lowercase, punctuation
import random

ENGLISH_LETTER_PROBABILITIES = {
		"a":0.08167, "b":0.01492, "c":0.02782, "d":0.04253, "e":0.12702, "f":0.02228, "g":0.02015, "h":0.06094, "i":0.06966, "j":0.00153, "k":0.00772, "l":0.04025, "m":0.02406,
		"n":0.06749, "o":0.07507, "p":0.01929, "q":0.00095, "r":0.05987, "s":0.06327, "t":0.09056, "u":0.02758, "v":0.00978, "w":0.02360, "x":0.00150, "y":0.01974, "z":0.00074}


class Encrypt():

	logger = logging.getLogger('encrypt')
	logging.basicConfig(level=logging.DEBUG)


	def __init__(self, plainText: str):
		self.plainText = plainText.lower()


	def __count_frequency(self):
		"""Creates dictionary of chars with frequency of their occurrences"""

		charsFreq = {char: 0 for char in ascii_lowercase}

		for char in self.plainText:
			if char != " " and char in charsFreq:
				charsFreq[char] += 1

		self.logger.info("Counted character frequency")

		return charsFreq

	def __remove_spaces(self):
		"""Replaces every space in text with randomly generated characters"""

		output = ""

		for char in self.plainText:
			if char != " ":
				output += char
			else:
				output += "".join(
					[random.choice(punctuation)] + [random.choice(ascii_lowercase)] + [random.choice(punctuation)])

		self.plainText = output
		self.logger.info("Removed spaces from text")


	def __monoalphabetic(self):
		"""Swaps letters from plaintext with high occurency to less frequent used ones"""

		ciphertext = ""

		sortedEnglishLetterProbabilities = list(
			dict(sorted(ENGLISH_LETTER_PROBABILITIES.items(), key=lambda item: item[1], reverse=True)).keys())
		reversedEnglishLetterProbabilities = list(
			dict(sorted(ENGLISH_LETTER_PROBABILITIES.items(), key=lambda item: item[1], reverse=False)).keys())

		dictOfCombinedChars = dict(zip(sortedEnglishLetterProbabilities, reversedEnglishLetterProbabilities))

		for char in self.plainText:
			if char != " ":
				ciphertext += dictOfCombinedChars[char]
			else:
				ciphertext += " "

		self.plainText = ciphertext

		self.logger.info("Encrypted text using monoalphabetic cipher" + ciphertext)


	def encrypt(self) -> str:
		"""Encrypts message using other methods"""

		self.__monoalphabetic()
		self.__remove_spaces()

		return self.plainText
