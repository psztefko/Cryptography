from fastapi import FastAPI
from src.Symmetric import Symmetric


app = FastAPI()

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