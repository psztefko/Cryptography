from fastapi import FastAPI

from src.Asymmetric import Asymmetric
from src.Symmetric import Symmetric


app = FastAPI()

#symmetric

symmetric = Symmetric()

@app.get("/symmetric/key/")
def symmetric_get_key():
    """Returns a randomly generated symmetric key in the form of HEX"""
    return symmetric.create_key()


@app.post("/symmetric/key/")
def symmetric_set_key(key: str):
    """Sets the symmetric key provided in the form of HEX in request on the server"""
    symmetric.set_key(key)


@app.post("/symmetric/encode/")
def symmetric_encode(message: str):
    """Sends a message and as a result returns it encrypted"""
    return symmetric.encode(message)


@app.post("/symmetric/decode/")
def symmetric_decode(message: str):
    """Sends a message and as a result returns it decrypted"""
    return symmetric.decode(message)

#asymmetric

asymmetric = Asymmetric()

@app.get("/asymmetric/key")
def get_asymmetric_key():
    """Returns new public and private key in the form of HEX (in JSON as dict) and sets it on the server"""

    return asymmetric.create_private_and_public_key()


@app.get("/asymmetric/key/ssh")
def get_ssh_key():
    """Returns public and private key in HEX format saved in OpenSSH format"""


@app.post("/asymmetric/key")
def set_asymmetric_key(privateKey: str, publicKey: str):
    """Sets the public and private key in the form of HEX (in JSON as dict)"""

    return asymmetric.set_key_values(privateKey, publicKey)


@app.post("/asymmetric/sign")
def sign_message(message: str):
    """Using the currently set private key, signs the message and returns it with the signed one"""

    return asymmetric.sign_message(message)


@app.post("/asymmetric/verify")
def verify_asymmetric_public_key():
    """Using the currently set public key, verify if the message was encrypted with it"""


@app.post("/asymmetric/encode")
def asymmetric_encode(message: str):
    """Sends a message and as a result returns it encrypted"""


@app.post("/asymmetric/decode")
def asymmetric_decode(message: str):
    """Sends a message and as a result returns it decrypted"""