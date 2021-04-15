from src.Decrypt import Decrypt
from src.Encrypt import Encrypt


testText = "sample text for testing purposes"

enc = Encrypt(testText)
encrypted = enc.encrypt()
dec = Decrypt(encrypted)
output = dec.decrypt()

assert output == testText