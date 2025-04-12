from . import config
import pymongo

def getDB(collection: str=None):
    if collection:
        return pymongo.MongoClient(config.DB["mongodb"]["connectionString"])[config.DB["mongodb"]["name"]]
    return pymongo.MongoClient(config.DB["mongodb"]["connectionString"])[config.DB["mongodb"]["name"][collection]]

