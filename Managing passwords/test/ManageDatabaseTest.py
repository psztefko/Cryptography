import sqlite3
from src.ManageDatabase import ManageDatabase



def test_init(self):
    db = ManageDatabase()
    self.assertIsInstance(db, ManageDatabase)


def __connect_with_database(self):
    """ create a database connection to the SQLite database
        :param None
        :return: Connection object or None
    """

    conn = None
    try:
        conn = sqlite3.connect('database.db')
    except Exception as e:
        self.logger.error('Error ocurred while connecting with database \nError message: %s' % e)

    return conn


def __create_table(self):
    """Creates table for testing purposes
        :param None
        :return None
    """

    conn = self.__connect_with_database()
    cursor = conn.cursor()
    try:
        cursor.execute('''SELECT count(*) FROM sqlite_master WHERE type='table' AND name='testTable' ''')
        cursor.execute("""CREATE TABLE testTable (testText text )""")

    except Exception as e:
        self.logger.error('Error ocurred while creating test database table \nError message: %s' % e)

    conn.commit()
    conn.close()

def __check_whether_test_table_exists(self):
    """Checks whether test table exists
        :param None
        :return True (if table exists) or False (if table doesn't exists)
    """

    conn = self.__connect_with_database()
    cursor = conn.cursor()
    try:
        cursor.execute('''SELECT count(*) FROM sqlite_master WHERE type='table' AND name='testTable' ''')

        if cursor.fetchone()[0] != 0:
            return True
        else:
            return False

    except Exception as e:
        self.logger.error('Error ocurred while checking if test database table exists \nError message: %s' % e)

    conn.commit()
    conn.close()


def __check_whether_table_is_empty(self):
    """Checks whether table is empty
        :param None
        :return True (if table is empty) or False (if table isn't empty)
    """

    conn = self.__connect_with_database()
    cursor = conn.cursor()
    try:

        rows = cursor.execute('''SELECT * FROM testTable''').fetchall()
        if len(rows) != 0:
            return False
        else:
            return True
    except Exception as e:
        self.logger.error('Error ocurred while checking if test table is empty \nError message: %s' % e)

    conn.commit()
    conn.close()


def __drop_testing_database(self):
    """Deletes table
        :param None
        :return None
    """

    conn = self.__connect_with_database()

    cursor = conn.cursor()
    try:
        cursor.execute('DROP TABLE testTable')
    except Exception as e:
        self.logger.error('Error ocurred while dropping table \nError message: %s' % e)

    conn.commit()
    conn.close()

def __insert_password(self, password):
    """Insert password into database
        :param password: string
        :return: None
    """

    conn = self.__connect_with_database()
    cursor = conn.cursor()
    try:
        # inserting password into database
        password = self.m.hash_password(password)
        query = """INSERT INTO testTable (testText) VALUES (?)"""
        cursor.execute(query, (password,))
        conn.commit()
        self.logger.info('Password succesfully added to database')
    except Exception as e:
        self.logger.error('Error ocurred while inserting password into database table \nError message: %s' % e)

    conn.commit()
    conn.close()

def test_create_table(self):
    self.__drop_testing_database()
    self.__create_table()
    self.assertTrue(self.__check_whether_test_table_exists())

def test_insert_password(self):
    if not self.__check_whether_test_table_exists():
        self.__create_table()
    self.__insert_password('testPassword')
    self.assertFalse(self.__check_whether_table_is_empty())