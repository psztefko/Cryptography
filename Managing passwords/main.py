from getpass import getpass
from src.Database import ManageDatabase
from src.ManagePassword import ManagePassword

db = ManageDatabase()

#db.create_table()
#db.insert_password('abba')

p = ManagePassword()

provided_password = input('Podaj hasło: ')

if input('Powtórz hasło: ') == provided_password:
    print('Hasła są takie same')
    #hash password
    #save to database
else:
    print('Hasła nie są takie same!')


#verify password

pas = p.hash_password(provided_password)

print(p.verify_password(pas, provided_password))

