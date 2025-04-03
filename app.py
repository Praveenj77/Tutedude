from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from pymongo import MongoClient
import os

app = Flask(__name__, static_folder='frontend')
CORS(app)

# Connect to MongoDB
client = MongoClient("mongodb+srv://dummy:1234@cluster0.lgtpggt.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client.todo_database  # Database name
collection = db.todo_items  # Collection name

# Serve the frontend (HTML, CSS, JS)
@app.route('/')
def serve_frontend():
    return send_from_directory('frontend', 'index.html')

# API Route for Submitting Data
@app.route('/api/submit', methods=['POST'])
def submit():
    try:
        data = request.json
        print("📩 Received Data:", data)  # Debugging

        # Insert into MongoDB
        result = collection.insert_one(data)
        print("✅ Data inserted with ID:", result.inserted_id)  # Debugging
        
        return jsonify({"message": "Data stored successfully", "id": str(result.inserted_id)}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# API Route to Retrieve All To-Do Items
@app.route('/api/todos', methods=['GET'])
def get_todos():
    try:
        todos = list(collection.find({}, {"_id": 0}))  # Exclude MongoDB _id from results
        return jsonify(todos), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, port=5000)
