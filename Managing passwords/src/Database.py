import sqlite3


class ManageDatabase():

    def __connect_with_database(self):
        conn = sqlite3.connect('database.db')
        return conn.cursor()


    def create_table(self):
        c = self.__connect_with_database()
        try:
            c.execute("""CREATE TABLE passwords (password VARCHAR )""")
        except Exception as e:
            print('Error ocurred while creating database table \nError: %s' % e)


    def insert_password(self, password):
        c = self.__connect_with_database()
        try:
            c.execute("""INSERT INTO passwords VALUES password""")
        except Exception as e:
            print('Error ocurred while inserting password into database table \nError: %s' % e)
