from fastapi import FastAPI
from cryptography.fernet import Fernet

app = FastAPI()

class Symmetric:


    symmetricKey :str

    @app.get("/symmetric/key")
    def get_key(self):
        """Returns a randomly generated symmetric key in the form of HEX"""
        return self.symmetricKey


    @app.post("/symmetric/key")
    def set_key(self):
        """Sets the symmetric key provided in the form of HEX in request on the server"""
        return Fernet.generate_key().hex()


    @app.post("/symmetric/encode")
    def symmetric_encode(self, message: str):
        """Sends a message and as a result returns it encrypted"""


    @app.post("/symmetric/decode")
    def symmetric_decode(self, message: str):
        """Sends a message and as a result returns it decrypted"""