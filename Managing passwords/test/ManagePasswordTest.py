from src.ManageDatabase import ManagePassword



def test_init(self):
    m = ManagePassword()
    assert self.assertIsInstance(m, ManagePassword) == True


def test_verify_password(self):
    m = ManagePassword()
    hashedPassword = m.hash_password('sample password')
    assert (m.verify_password(hashedPassword, 'sample password')) == True


