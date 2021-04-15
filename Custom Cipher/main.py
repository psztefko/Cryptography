from src.Decrypt import Decrypt
from src.Encrypt import Encrypt


if __name__ == '__main__':

    f = open("sampleText.txt", "r")

    enc = Encrypt(f.read())
    encrypted = enc.encrypt()
    dec = Decrypt(encrypted)
    decrypted = dec.decrypt()

    print("Encrypted message: " + encrypted)
    print("Decrypted message: " + decrypted)