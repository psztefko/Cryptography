import sqlite3


class ManageDatabase():

    def connect_with_database(self):
        conn = sqlite3.connect('database.db')
        return conn.cursor()


    def create_table(self):
        c = self.connect_with_database()
        try:
            c.execute("""CREATE TABLE passwords (password VARCHAR )""")
        except Exception as e:
            print('Error ocurred while creating database table \n Error: %s' % e)

    def insert_password(self, password):
        try:
            self.c.execute("""INSERT INTO passwords VALUE password""")
        except Exception as e:
            print('Error ocurred while inserting password into database table \n Error: %s' % e)
