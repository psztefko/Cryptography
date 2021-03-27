# from fastapi import FastAPI
# from cryptography.fernet import Fernet
#
# app = FastAPI()
#
# class Asymmetric:
#
#     @app.get("/asymmetric/key")
#     def get_asymmetric_key(self):
#         """Returns new public and private key in the form of HEX (in JSON as dict) and sets it on the server"""
#
#
#     @app.get("/asymmetric/key/ssh")
#     def get_ssh_key(self):
#         """Returns public and private key in HEX format saved in OpenSSH format"""
#
#
#     @app.post("/asymmetric/key")
#     def set_asymmetric_key(self):
#         """Sets the public and private key in the form of HEX (in JSON as dict)"""
#
#
#     @app.post("/asymmetric/verify")
#     def verify_asymmetric_key(self):
#         """Using the currently set private key, signs the message and returns it with the signed one"""
#
#
#     @app.post("/asymmetric/sign")
#     def verify_asymmetric_public_key(self):
#         """Using the currently set public key, verify if the message was encrypted with it"""
#
#
#     @app.post("/asymmetric/encode")
#     def asymmetric_encode(self, message: str):
#         """Sends a message and as a result returns it encrypted"""
#
#
#     @app.post("/asymmetric/decode")
#     def asymmetric_decode(self, message: str):
#         """Sends a message and as a result returns it decrypted"""