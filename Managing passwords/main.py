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
# print(p.verify_password('185065c9e390d7d4466cf580e142dfc05680929e8118b6727bda1fe5ec8afa5802287a1ef8e3a6ce45b5b0a5a09bec3db467562bee62773433cfea028ddb024b2834c8f92f66cca88745e1410133e7da8ba2ac4a6c7ffa6b351790eaa935c684', provided_password))
# print(provided_password)
# print(password)

db.insert_password(provided_password)

