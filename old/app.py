from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app)

JSON_FILE = "data.json"

# Function to read data from JSON file
def read_json():
    if not os.path.exists(JSON_FILE):
        return {"data": []}  # Return an empty structure if file doesn't exist
    with open(JSON_FILE, "r") as file:
        return json.load(file)

# Function to write data to JSON file
def write_json(new_data):
    data = read_json()
    data["data"].append(new_data)
    with open(JSON_FILE, "w") as file:
        json.dump(data, file, indent=4)

@app.route("/api/submit", methods=["POST"])
def submit():
    try:
        data = request.json
        write_json(data)  # Save data to JSON instead of MongoDB
        return jsonify({"message": "Data saved successfully"}), 201
    except Exception as e:
        return jsonify({"message": "Error saving data", "error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, port=5000)
