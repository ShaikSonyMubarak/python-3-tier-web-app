from flask import Flask, jsonify
from pymongo import MongoClient
import os

app = Flask(__name__)

# MongoDB connection
mongo_url = os.getenv("MONGO_URL", "mongodb://mongo:27017/")
client = MongoClient(mongo_url)
db = client["testdb"]
collection = db["items"]

@app.route('/')
def home():
    return "Python Backend Running 🚀"

@app.route('/data')
def get_data():
    data = list(collection.find({}, {"_id": 0}))
    return jsonify(data)

@app.route('/add')
def add_data():
    collection.insert_one({"name": "Docker User"})
    return "Data Added ✅"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
