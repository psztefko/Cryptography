from src.Decrypt import Decrypt
from src.Encrypt import Encrypt


if __name__ == '__main__':

    enc = Encrypt("Tekst testowy losowy ruzny")

    print(enc.encrypt())

    dec = Decrypt(enc.encrypt())

    print(dec.decrypt())