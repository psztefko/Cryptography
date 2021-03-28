from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa

class Asymmetric:


    keys = {
        "privateKey": "",
        "publicKey": ""
    }

    def __update_keys(self, privateKey):
        self.keys["privateKey"] = privateKey.private_bytes(encoding=serialization.Encoding.PEM,
                                                           format=serialization.PrivateFormat.TraditionalOpenSSL,
                                                           encryption_algorithm=serialization.NoEncryption())
        self.keys["publicKey"] = hex(privateKey.public_key().public_bytes(encoding=serialization.Encoding.PEM,
                                                                      format=serialization.PublicFormat.SubjectPublicKeyInfo))

    def create_private_and_public_key(self):
        self.__update_keys(rsa.generate_private_key(public_exponent=65537, key_size=2048))
        return self.keys
