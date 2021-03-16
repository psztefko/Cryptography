import sqlite3


class ManageDatabase():
    """Class that manage database containing passwords"""

    def __connect_with_database(self):
        conn = sqlite3.connect('database.db')
        return conn.cursor()

    def create_table(self):
        c = self.__connect_with_database()
        try:
            c.execute('''SELECT count(*) FROM sqlite_master WHERE type='table' AND name='passwords' ''')

            if c.fetchone()[0] == 0:
                c.execute("""CREATE TABLE passwords (password text )""")
                print('Table succesfully created')
            else:
                print('Table already exists')

        except Exception as e:
            print('Error ocurred while creating database table \nError: %s' % e)


    def insert_password(self, password):
        c = self.__connect_with_database()
        try:
            c.execute("""INSERT INTO passwords VALUES (password)""")
        except Exception as e:
            print('Error ocurred while inserting password into database table \nError: %s' % e)
