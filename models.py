from pymongo import MongoClient

# Connect to MongoDB server (localhost default)
client = MongoClient("mongodb://localhost:27017/")

# Select a database
db = client['mydatabase']

# Select a collection
collection = db['mycollection']

# Insert a document
collection.insert_one({"name": "Alice", "age": 25})

# Fetch a document
document = collection.find_one({"name": "Alice"})
print(document)
