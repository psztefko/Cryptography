from src import Symmetric

symmetric = Symmetric()


def test_initialization():
    """Tests if instance is properly initialized"""

    assert symmetric != None


def test_create_key():
    """Tests if key is being created"""

    assert symmetric.create_key() != ""


def test_set_key():
    """Tests if key is being properly set"""

    assert symmetric.set_key("test") == "test"


def test_encode():
    """Tests if message is being encoded properly"""


def test_decode():
    """Tests if message is being decoded properly"""