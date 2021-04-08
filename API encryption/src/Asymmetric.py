import base64
import hashlib

from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
import logging


class Asymmetric:

    logger = logging.getLogger('asymmetric')
    logging.basicConfig(level=logging.DEBUG)

    privateKey = None
    publicKey = None

    def __init__(self):

        keys = self.__generate_rsa_keys()
        self.privateKey = keys["privateKey"]
        self.publicKey = keys["publicKey"]


    def __generate_rsa_keys(self):
        """Creates rsa keys"""

        if self.privateKey == None and self.publicKey == None:
            privateKey = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
            backend=default_backend()
            )
            publicKey = privateKey.public_key()

            self.logger.info("RSA keys created succesfully")

        return {"privateKey": privateKey, "publicKey": publicKey}


    def __generate_pem_keys(self) -> dict:
        """Convert keys to pem format"""

        privatePem = self.privateKey.private_bytes(encoding=serialization.Encoding.PEM,
                                                                   format=serialization.PrivateFormat.TraditionalOpenSSL,
                                                                   encryption_algorithm=serialization.NoEncryption())
        publicPem = self.privateKey.public_key().public_bytes(encoding=serialization.Encoding.PEM,
                                                                              format=serialization.PublicFormat.SubjectPublicKeyInfo)

        self.logger.info("Pem keys created succesfully")

        return {"privatePem": privatePem, "publicPem": publicPem}

    def __generate_hex_keys(self) -> dict:
        """Convert keys from pem to hex format"""

        pemKeys = self.__generate_pem_keys()

        privateHex = pemKeys["privatePem"].hex()
        publicHex = pemKeys["publicPem"].hex()

        self.logger.info("Hex keys created succesfully")

        return {"privatePem": privateHex, "publicPem": publicHex}


    def create_private_and_public_key(self) -> dict:
        """"Generates private key and passes it to method that updates both keys values"""

        return self.__generate_hex_keys()


    def set_key_values(self, privateKey, publicKey) -> dict:
        """Takes the private key and based on it's value generates public one"""

        self.privateKey = privateKey
        self.publicKey = publicKey

        self.logger.info("Key values setted successfully")

        return self.keys


    def get_keys_in_ssh(self) -> dict:
        """Returns keys in OpenSSH format"""

        privateSSH = self.privateKey.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.OpenSSH,
            encryption_algorithm=serialization.NoEncryption()
        ).hex()

        publicSSH = self.publicKey.public_bytes(
            encoding=serialization.Encoding.OpenSSH,
            format=serialization.PublicFormat.OpenSSH
        ).hex()

        return {
            'privateSSH': privateSSH,
            'publicSSH': publicSSH
        }

    def sign_message(self, message) -> bytes:
        """Takes message and signs it using private key"""

        prehashed = hashlib.sha256(message.encode('ascii')).hexdigest()

        if self.privateKey != None:
            self.signature = self.privateKey.sign(
                bytes(prehashed.encode('ascii')),
                padding.PSS(
                    mgf=padding.MGF1(hashes.SHA256()),
                    salt_length=padding.PSS.MAX_LENGTH
                ),
                hashes.SHA256()
            )
            return base64.b64encode(self.signature)
        else:
            self.logger.error("Private key value not set")


    def verify_message(self, message: str, signature: str) -> bool:
        """Using the currently set public key, verifies if the message was encrypted with it"""

        decodedSignature = base64.b64decode(signature)
        prehashedMessage = hashlib.sha256(message.encode('ascii')).hexdigest()

        try:
            self.publicKey.verify(
                decodedSignature,
                bytes(prehashedMessage.encode('ascii')),
                padding.PSS(
                    mgf=padding.MGF1(hashes.SHA256()),
                    salt_length=padding.PSS.MAX_LENGTH),
                hashes.SHA256())
        except InvalidSignature:
            self.logger.error("Invalid Signature")
            return False
        else:
            self.logger.info("Signature verified successfully")
            return True


    def encrypt_message(self, message: str) -> bytes:
        """Gets a message and returns it encrypted"""

        try:
            return base64.b64encode(self.publicKey.encrypt(
                message.encode(),
                padding.OAEP(
                    mgf=padding.MGF1(algorithm=hashes.SHA256()),
                    algorithm=hashes.SHA256(),
                    label=None
                )
            ))
        except:
            self.logger.error("Error ocurred while encrypting message")


    def decrypt_messege(self, message: str) -> bytes:
        """Gets encrypted message and returns it decrypted"""

        return self.privateKey.decrypt(
            base64.b64decode(message),
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
