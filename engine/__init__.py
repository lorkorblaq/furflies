from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv, find_dotenv
import os

# Load environment variables from .env file
load_dotenv(find_dotenv())

# Get the MongoDB credentials from environment variables
user = os.getenv('MONGODB_USER')
password = os.getenv('MONGODB_PASSWORD')

# Ensure user and password are retrieved correctly
if not user or not password:
    raise ValueError("Environment variables for MongoDB credentials are not set.")

# Connection URI with additional TLS options
# uri_development = f"mongodb+srv://{user}:{password}@project-cluster.hrihk98.mongodb.net/?retryWrites=true&w=majority"
uri_development = f"mongodb+srv://{user}:{password}@clinicalx.aqtbwah.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri_development)

try:
    # Send a ping to confirm a successful connection
    client.admin.command('ping')
    print("You successfully connected to Perpetual MongoDB!")
except Exception as e:
    print(f"An error occurred: {e}")

# Access the desired database
# db_clinical = client['project-cluster']
db_clinical = client['clinicalx']