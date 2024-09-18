import certifi
from mongoengine import connect, disconnect
import os

MONGO_URI = os.getenv("MONGO_URI")

def init_db():
    connect(
        host=MONGO_URI,
        tlsCAFile=certifi.where(),
        alias='default'
    )

def close_db():
    disconnect(alias='default')

init_db()