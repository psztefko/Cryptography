from fastapi import FastAPI

app = FastAPI()


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
