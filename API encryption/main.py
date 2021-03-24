from fastapi import FastAPI

app = FastAPI()

#symmetric

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/symmetric/key")
def get_key():
    """Returns a randomly generated symmetric key in the form of HEX"""
    #return key

@app.post("/symmetric/key")
def set_key():
    """Sets the symmetric key provided in the form of HEX in request on the server"""

@app.post("/symmetric/encode")
def symmetric_encode(message: str):
    """Sends a message and as a result returns it encrypted"""

@app.post("/symmetric/decode")
def symmetric_decode(message: str):
    """Sends a message and as a result returns it decrypted"""


#asymmetric

@app.get("/asymmetric/key")
def get_asymmetric_key():
    """Returns new public and private key in the form of HEX (in JSON as dict) and sets it on the server"""

@app.get("/asymmetric/key/ssh")
def get_ssh_key():
    """Returns public and private key in HEX format saved in OpenSSH format"""

@app.post("/asymmetric/key")
def set_asymmetric_key():
    """Sets the public and private key in the form of HEX (in JSON as dict)"""

app.post("/asymmetric/verify")
def verify_asymmetric_key():
    """Using the currently set private key, signs the message and returns it with the signed one"""

app.post("/asymmetric/sign")
def verify_asymmetric_public_key():
    """Using the currently set public key, verify if the message was encrypted with it"""

app.post("/asymmetric/encode")
def asymmetric_encode(message: str):
    """Sends a message and as a result returns it encrypted"""

app.post("/asymmetric/decode")
def asymmetric_decode(message: str):
    """Sends a message and as a result returns it decrypted"""