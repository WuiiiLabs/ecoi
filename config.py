from dotenv import load_dotenv
import os, pymongo

load_dotenv()


DB = pymongo.MongoClient(os.getenv("MONGODB_CONNECTION_STRING"))['Ecoi [Beta]']