from unittest import TestCase
from src.ManageDatabase import ManageDatabase


class ManageDatabaseTest():

    def test_init(self):
        db = ManageDatabase()
        self.assertIsInstance(db, ManageDatabase)

