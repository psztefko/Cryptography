from src.Decrypt import Decrypt
from src.Encrypt import Encrypt


if __name__ == '__main__':

    enc = Encrypt("Tekst testowy losowy ruzny")
    encrypted = enc.encrypt()
    dec = Decrypt(encrypted)

    print("Encrypted message: " + encrypted)
    print("Decrypted message: " + dec.decrypt())