from flask import Flask, request
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient("mongodb+srv://dummy:1234@cluster0.lgtpggt.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client.test
collection = db.todo_items

@app.route("/submittodoitem", methods=["POST"])
def submit_todo():
    data = request.json
    item = {
        "itemName": data["itemName"],
        "itemDescription": data["itemDescription"],
    }
    collection.insert_one(item)
    return {"message": "Item added successfully"}, 201

if __name__ == "__main__":
    app.run(debug=True)
