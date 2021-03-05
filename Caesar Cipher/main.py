from CaesarCipher import CaesarCipher


string = input('Wprowadź tekst do zaszyfrowania: ')
key = int(input('Wprowadź klucz: '))

cc = CaesarCipher()

# print('Zaszyfrowana wiadomość: ' + cc.encrypt(string, key))
#
# print('Odszyfrowana wiadomość: ' + cc.decrypt(string, key))

x = int(input('Złam szyfr automatycznie (1) lub manualnie (2): '))

if x == 1:
    print('Odszyfrowana wiadomość: ' + cc.automateHack(cc.createDictionaryOfPossibilities(cc.encrypt(string, key))))
elif x == 2:
    dictionaryOfPossibilities = cc.createDictionaryOfPossibilities(cc.encrypt(string, key))
    for key, value in dictionaryOfPossibilities.items():
        print(key, ' : ', value)

    choice = int(input('Wybierz odszyfrowaną wiadomość: '))
    print(dictionaryOfPossibilities.get(choice))

else:
    print('Niewłaściwy wybór!')










