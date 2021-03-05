from unittest import TestCase

from CaesarCipher import CaesarCipher


class CaesarCipherTest(TestCase):


    def test_init(self):
        cc = CaesarCipher()
        self.assertIsInstance(cc, CaesarCipher)

    def test_encrypt(self):
        cc = CaesarCipher()
        self.assertEqual(cc.encrypt('a',1 ), 'b')

    def test_encrypt_parse_character(self):
        cc = CaesarCipher()
        self.assertEqual(cc.encrypt('A', 1), 'b')

    def test_encrypt_boundary_value(self):
        cc = CaesarCipher()
        self.assertEqual(cc.encrypt('z', 1), 'a')

    # checking if all of dictionary values are unique
    def test_possibilities_dictionary(self):
        cc = CaesarCipher()
        self.assertEqual(len(set(cc.createDictionaryOfPossibilities('a'))), 26)