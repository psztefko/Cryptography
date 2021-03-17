from unittest import TestCase
from src.ManageDatabase import ManagePassword


class ManagePasswordTest():


    def test_init(self):
        m = ManagePassword()
        self.assertIsInstance(m, ManagePassword)


    def test_verify_password(self):
        m = ManagePassword()
        hashedPassword = m.hash_password('sample password')
        m.assertTrue(m.verify_password(hashedPassword, 'sample password'))