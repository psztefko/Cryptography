from fastapi import FastAPI
from src.Blockchain import Blockchain
import json


app = FastAPI()

blockchain = Blockchain()

@app.get("/chain/")
def get_chain():
    chain_data = []
    for block in blockchain.chain:
        chain_data.append(block.__dict__)
    return json.dumps({"length": len(chain_data),
                       "chain": chain_data})

@app.get("/add_block/")
def add_block(sender: str, recipient: str, amount: str):
    transaction = {
        'sender': sender,
        'recipient': recipient,
        'amount': amount
    }
    blockchain.add_new_transaction(transaction)
    return blockchain.last_block

@app.get("/mine/")
def mine():
    return blockchain.mine()



















