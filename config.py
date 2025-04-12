from dotenv import load_dotenv
import os

load_dotenv()


DB = {
    "mongodb": {
        "name": "Ecoi",
        "connectionString": os.getenv("MONGODB_CONNECTION_STRING")
    },
}