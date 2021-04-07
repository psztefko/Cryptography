from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
import logging


class Asymmetric:

    logger = logging.getLogger('database')
    logging.basicConfig(level=logging.DEBUG)

    def __init__(self):
        self.keys = {
            "privateKey": None,
            "publicKey": None
        }

        self.pemKeys = {
            "privateKey": None,
            "publicKey": None
        }

        self.hexKeys = {
            "privateKey": "",
            "publicKey": ""
        }

    def __update_keys(self):
        """Updates key values in dictionary"""

        self.keys["privateKey"] = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
        )

        self.keys["publicKey"] = self.keys["privateKey"].public_key()

        self.logger.info("Keys updated succesfully")

        self.__update_pem_keys()

        self.logger.info("Pem keys updated succesfully")

        self.__update_hex_keys()

        self.logger.info("Hex keys updated succesfully")

    def __update_pem_keys(self):
        """Convert keys to pem format"""

        self.pemKeys["privateKey"] = self.keys["privateKey"].private_bytes(encoding=serialization.Encoding.PEM,
                                                                   format=serialization.PrivateFormat.TraditionalOpenSSL,
                                                                   encryption_algorithm=serialization.NoEncryption())
        self.pemKeys["publicKey"] = self.keys["privateKey"].public_key().public_bytes(encoding=serialization.Encoding.PEM,
                                                                              format=serialization.PublicFormat.SubjectPublicKeyInfo)


    def __update_hex_keys(self):
        """Convert keys to hex format"""

        self.hexKeys["privateKey"] = self.pemKeys["privateKey"].hex()
        self.hexKeys["publicKey"] = self.pemKeys["publicKey"].hex()

    # def __unhex_keys(self):
    #     """Convert keys from hex to binary format"""
    #
    #     self.pemKeys["privateKey"] = self.pemKeys["privateKey"].decode(hex)
    #     self.pemKeys["publicKey"] = self.pemKeys["publicKey"].decode(hex)


    def create_private_and_public_key(self):
        """"Generates private key and passes it to method that updates both keys values"""

        self.__update_keys()

        return self.hexKeys

    def set_key_values(self, privateKey, publicKey):
        """Takes the private key and based on it's value generates public one"""

        self.keys["privateKey"] = privateKey
        self.keys["publicKey"] = publicKey

        self.logger.info("Key values setted successfully")

        return self.keys

    def sign_message(self, message):
        """Takes message and signs it using private key"""

        self.__update_keys()

        return self.keys["privateKey"].sign(
            message,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
