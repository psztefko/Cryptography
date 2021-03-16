import sqlite3
from src.ManagePassword import ManagePassword

class ManageDatabase():
    """Class that manage database containing passwords"""

    def __init__(self):
        self.m = ManagePassword()


    def __connect_with_database(self):
        return sqlite3.connect('database.db')

    def create_table(self):
        conn = self.__connect_with_database()
        cursor = conn.cursor()
        try:
            cursor.execute('''SELECT count(*) FROM sqlite_master WHERE type='table' AND name='passwords' ''')

            if cursor.fetchone()[0] == 0:
                cursor.execute("""CREATE TABLE passwords (password text )""")
                conn.commit()
                print('Table succesfully created')
            else:
                print('Table already exists')

        except Exception as e:
            print('Error ocurred while creating database table \nError: %s' % e)

        conn.close()


    def __check_whether_password_exists(self, provided_password):
        conn = self.__connect_with_database()
        cursor = conn.cursor()
        try:
            rows = cursor.execute('''SELECT * FROM passwords''').fetchall()
            x = slice(2, 194)
            for row in rows:
                row = str(row[x])
                print(self.m.verify_password(row, provided_password))
                if self.m.verify_password(row, provided_password):
                    return True
            return False
        except Exception as e:
            print('Error ocurred while checking if password is already in database \nError message: %s' % e)

        conn.close()


    def insert_password(self, password):
        conn = self.__connect_with_database()
        cursor = conn.cursor()
        try:
            if self.__check_whether_password_exists(password):
                print('This password already exists in database')
            else:
                password = self.m.hash_password(password)
                print(password)
                query = """INSERT INTO passwords (password) VALUES (?)"""
                cursor.execute(query, (password,))
                conn.commit()
                print('Password succesfully added to database')
        except Exception as e:
            print('Error ocurred while inserting password into database table \nError message: %s' % e)

        conn.close()
