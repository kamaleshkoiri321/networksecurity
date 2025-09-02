import os
from dotenv import load_dotenv
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

# Load environment variables from .env file
load_dotenv()

# Get MongoDB URI from environment
uri = os.getenv("MONGO_DB_URL")

if not uri:
    raise ValueError("MONGO_DB_URL not found in environment. Please set it in your .env file.")

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print(" Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(" Connection failed:", e)
