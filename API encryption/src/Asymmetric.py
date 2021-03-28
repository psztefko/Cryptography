from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
import logging


class Asymmetric:

    logger = logging.getLogger('database')
    logging.basicConfig(level=logging.DEBUG)

    keys = {
        "privateKey": "",
        "publicKey": ""
    }

    def __update_keys(self, privateKey):
        """Updates key values in dictionary"""

        self.keys["privateKey"] = privateKey.private_bytes(encoding=serialization.Encoding.PEM,
                                                           format=serialization.PrivateFormat.TraditionalOpenSSL,
                                                           encryption_algorithm=serialization.NoEncryption()).hex()
        self.keys["publicKey"] = privateKey.public_key().public_bytes(encoding=serialization.Encoding.PEM,
                                                                      format=serialization.PublicFormat.SubjectPublicKeyInfo).hex()
        self.logger.info("Keys updated succesfully")


    def create_private_and_public_key(self):
        """"Generates private key and passes it to method that updates both keys values"""

        self.__update_keys(rsa.generate_private_key(public_exponent=65537, key_size=2048))
        return self.keys

    def set_key_values(self, privateKey, publicKey):
        """Takes the private key and based on it's value generates public one"""
        self.keys["privateKey"] = privateKey
        self.keys["publicKey"] = publicKey

        self.logger.info("Key values setted successfully")

        return self.keys

    def sign_message(self, message):
        """Takes message and signs it using private key"""

        return self.keys["privateKey"].sign(
            message,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
