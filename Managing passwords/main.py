from getpass import getpass
from src.Database import ManageDatabase
from src.ManagePassword import ManagePassword

db = ManageDatabase()
db.create_table()

provided_password = input('Podaj hasło: ')

while True:
    if input('Powtórz hasło: ') == provided_password:
        break
    else:
        print('Hasła nie są takie same!')

p = ManagePassword()

# password = p.hash_password(provided_password)
# print(p.verify_password('6456ae47d19fe64c0b33325ca5955829eb755520f5c54108ccb55c48a99ecbe101051b4a62cb0a2724245e14202dd2c21cbdeebddbe71782c930f658288e598b79d1c0da296435e3c02f1a1ae61cf2cb934ac228253e837322a37f67ed1241c7', provided_password))
# print(provided_password)
# print(password)

db.insert_password(provided_password)

