from getpass import getpass
from src.ManageDatabase import ManageDatabase


if __name__ == '__main__':

    provided_password = input('Podaj hasło: ')

    while True:
        if input('Powtórz hasło: ') == provided_password:
            break
        else:
            print('Hasła nie są takie same!')

    db = ManageDatabase()
    db.create_table()
    db.insert_password(provided_password)

