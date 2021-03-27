from cryptography.fernet import Fernet

class Symmetric:


    key :str

    def create_key(self):
        return Fernet.generate_key().hex()

    def set_key(self, key):
        self.key = key

    def encode(self, message: str) -> hex:
        return Fernet(bytearray.fromhex(self.key)).encrypt(message).hex()

    def decode(self, message: str):
        return Fernet(self.key).decrypt(message).hex()