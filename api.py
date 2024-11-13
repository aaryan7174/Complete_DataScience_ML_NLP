###Put and Delete-HTTP Verbs
###Working with API's--Json
from flask import Flask, jsonify, request
app=Flask(__name__)

#Initial data in my to do List or database
items=[
    {"id":1, "name":"item1","description":"This is item 1"},
    {"id":2, "name":"item2","description":"This is item 2"},
]

@app.route('/')
def home():
    return "Welcome to my to do list"

#Get all items
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items)

#Get a specific item by id
@app.route('/items/<int:id>', methods=['GET'])
def get_item(id):
    for i in range(len(items)):
        if items[i]['id']==id:
            return jsonify(items[i])
    return jsonify({"error":"Item not found"})

#POST-Create a new item
@app.route('/items', methods=['POST'])
def create_item():
    if not request.json or 'name' not in request.json:
        return jsonify({"error": "Item not found"})
    new_item = {
        "id": items[-1]["id"] + 1 if items else 1,
        "name": request.json["name"],
        "description": request.json.get("description", "")
    }
    items.append(new_item)
    return jsonify(new_item)

# Put-Update an item
@app.route('/items/<int:id>', methods=['PUT'])
def update_item(id):  # Change item_id to id here
    item = next((item for item in items if item['id'] == id), None)
    if item is None:
        return jsonify({"error": "Item not found"})
    item['name'] = request.json.get('name', item['name'])
    item['description'] = request.json.get('description', item['description'])
    return jsonify(item)

# Delete-Delete an item
@app.route('/items/<int:id>', methods=['DELETE'])
def delete_item(id):  # Change item_id to id here
    global items
    items = [item for item in items if item['id'] != id]
    return jsonify({"message": "Item deleted successfully"})

if __name__ == '__main__':
    app.run(debug=True)