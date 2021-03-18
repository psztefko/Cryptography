import sqlite3
from src.ManagePassword import ManagePassword
import logging

class ManageDatabase():
    """Class that manage database containing passwords"""

    logger = logging.getLogger('database')
    logging.basicConfig(level=logging.DEBUG)

    def __init__(self):
        self.m = ManagePassword()

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

    def create_table(self):
        """Checking if table for passwords exists and if not, creates one
            :param None
            :return None
        """

        conn = self.__connect_with_database()
        cursor = conn.cursor()
        try:
            #
            cursor.execute('''SELECT count(*) FROM sqlite_master WHERE type='table' AND name='passwords' ''')

            if cursor.fetchone()[0] == 0:
                cursor.execute("""CREATE TABLE passwords (password text )""")
                conn.commit()
                self.logger.info('Table succesfully created')
            else:
                self.logger.info('Table already exists')

        except Exception as e:
            self.logger.error('Error ocurred while creating database table \nError message: %s' % e)

        conn.close()


    def __check_whether_password_exists(self, provided_password):
        """Checking if password already is in database
            :param provided_password: string
            :return bool True(if succeed) or False (in case of failure)
        """

        conn = self.__connect_with_database()
        cursor = conn.cursor()
        try:
            # gets all records from database into tuple
            rows = cursor.execute('''SELECT * FROM passwords''').fetchall()
            if len(rows) != 0:
                for row in rows[0]:
                    # compare every record from database with user input
                    if self.m.verify_password(row, provided_password):
                        return True
                return False
            else:
                return False
        except Exception as e:
            self.logger.error('Error ocurred while checking if password is already in database \nError message: %s' % e)
        conn.close()


    def insert_password(self, password):
        """Insert password into database if it's unique
            :param password: string
            :return: None
        """

        conn = self.__connect_with_database()
        cursor = conn.cursor()
        try:
            if self.__check_whether_password_exists(password):
                self.logger.info('This password already exists in database')
            else:
                # inserting password into database
                password = self.m.hash_password(password)
                query = """INSERT INTO passwords (password) VALUES (?)"""
                cursor.execute(query, (password,))
                conn.commit()
                self.logger.info('Password succesfully added to database')
        except Exception as e:
            self.logger.error('Error ocurred while inserting password into database table \nError message: %s' % e)

        conn.close()