from fastapi import FastAPI
from src.Asymmetric import Asymmetric
from src.Symmetric import Symmetric


app = FastAPI()

#symmetric

symmetric = Symmetric()

@app.get("/symmetric/key/", tags=["Get Methods", "Symmetric Methods"])
async def symmetric_get_key():
    """Returns a randomly generated symmetric key in the form of HEX"""
    return symmetric.create_key()


@app.post("/symmetric/key/", tags=["Post Methods", "Symmetric Methods"])
async def symmetric_set_key(key: str):
    """Sets the symmetric key provided in the form of HEX in request on the server"""
    symmetric.set_key(key)


@app.post("/symmetric/encode/", tags=["Post Methods", "Symmetric Methods"])
async def symmetric_encode(message: str):
    """Sends a message and as a result returns it encrypted"""
    return symmetric.encode(message)


@app.post("/symmetric/decode/", tags=["Post Methods", "Symmetric Methods"])
async def symmetric_decode(message: str):
    """Sends a message and as a result returns it decrypted"""
    return symmetric.decode(message)

#asymmetric

asymmetric = Asymmetric()

@app.get("/asymmetric/key", tags=["Get Methods", "Asymmetric Methods"])
async def get_asymmetric_key():
    """Returns new public and private key in the form of HEX (in JSON as dict) and sets it on the server"""

    return asymmetric.create_private_and_public_key()


@app.get("/asymmetric/key/ssh", tags=["Get Methods", "Asymmetric Methods"])
async def get_ssh_key():
    """Returns public and private key in HEX format saved in OpenSSH format"""

    return asymmetric.get_keys_in_ssh()


@app.post("/asymmetric/key", tags=["Post Methods", "Asymmetric Methods"])
async def set_asymmetric_key(privateKey: str, publicKey: str):
    """Sets the public and private key in the form of HEX (in JSON as dict)"""

    return asymmetric.set_key_values(privateKey)


@app.post("/asymmetric/sign", tags=["Post Methods", "Asymmetric Methods"])
async def sign_message(message: str):
    """Using the currently set private key, signs the message and returns it with the signed one"""

    return asymmetric.sign_message(message)


@app.post("/asymmetric/verify", tags=["Post Methods", "Asymmetric Methods"])
async def verify_signed_message(message: str, signature: str):
    """Using the currently set public key, verify if the message was encrypted with it"""

    return asymmetric.verify_message(message, signature)


@app.post("/asymmetric/encode", tags=["Post Methods", "Asymmetric Methods"])
async def asymmetric_encode(message: str):
    """Sends a message and as a result returns it encrypted"""

    return asymmetric.encrypt_message(message)


@app.post("/asymmetric/decode", tags=["Post Methods", "Asymmetric Methods"])
async def asymmetric_decode(message: str):
    """Sends a message and as a result returns it decrypted"""

    return asymmetric.decrypt_messege(message)