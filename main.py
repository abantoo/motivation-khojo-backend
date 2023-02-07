from typing import Union
from fastapi import FastAPI
import pymongo
import json

app = FastAPI()

data = json.load(open("config.json", "r"))

# Replace the uri string with your MongoDB deployment's connection string from .
conn_str = f"mongodb+srv://{data['username']}:{data['password']}@{data['cluster']}/?retryWrites=true&w=majority"

print(conn_str)

# set a 5-second connection timeout
client = pymongo.MongoClient(conn_str, serverSelectionTimeoutMS=5000)

try:
    print(client.get_database())
except Exception:
    print("Unable to connect to the server.")


responseObject = [{
    "username": "orion",
    "firstname": "Orio"
}]


@app.get("/")
async def read_root():
    return responseObject


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
