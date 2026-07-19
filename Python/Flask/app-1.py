from flask import Flask, jsonify, request
app=Flask(__name__)
@app.route('/api/home', methods=['get'])
def home():
    return jsonify({'message': 'Welcome to the home page!'})
#Create--? POST Method,Read-->GET Method,Update-->PUT Method,Delete-->DELETE Method
#Status Codes: 200-->Success, 201-->Created, 400-->Bad Request, 401-->Unauthorized,
# 403-->Forbidden, 404-->Not Found, 500-->Internal Server Error

contacts=[
    {'id': 1, 'name': 'John Doe', 'email': 'john.doe@example.com'},
    {'id': 2, 'name': 'Jane Smith', 'email': 'jane.smith@example.com'},
    {'id': 3, 'name': 'Alice Johnson', 'email': 'alice.johnson@example.com'},
    {'id': 4, 'name': 'Bob Brown', 'email': 'bob.brown@example.com'},
    {'id': 5, 'name': 'Charlie Davis', 'email': 'charlie.davis@example.com'}
]

@app.route('/api/contacts', methods=['GET'])
def get_contacts():
    return jsonify(contacts), 200  
@app.route('/api/contacts/<int:contact_id>', methods=['GET'])
def find_contact(contact_id):
    for contact in contacts:
        if contact['id'] == contact_id:
            return contact, 200
    return jsonify({'error': 'Contact not found'}), 404
#  curl -X POST http://127.0.0.1:5000/api/contacts -H "Content-Type: application/json" -d '{"name":"Umesh Kumar","email": "umesh.kumar@example.com"}'

@app.route('/api/contacts', methods=['POST'])
def add_contact():  
    new_contact = request.get_json()
    if not new_contact or 'name' not in new_contact or 'email' not in new_contact:
        return jsonify({'error': 'Invalid input'}), 400
    new_contact['id'] = max(contact['id'] for contact in contacts) + 1 if contacts else 1
    contacts.append(new_contact)
    return jsonify(new_contact), 201
#  curl -X PUT http://127.0.0.1:5000/api/contacts/1 -H "Content-Type: application/json" -d '{"id": 8, "name":"Aman Kumar","email": "aman.kumar@example.com"}'
@app.route('/api/contacts/<int:contact_id>', methods=['PUT'])
def update_contact(contact_id):
    updated_contact = request.get_json()
    if not updated_contact or 'name' not in updated_contact or 'email' not in updated_contact:
        return jsonify({'error': 'Invalid input'}), 400
    for contact in contacts:
        if contact['id'] == contact_id:
            contact['name'] = updated_contact['name']
            contact['email'] = updated_contact['email']
            return jsonify(contact), 200
    return jsonify({'error': 'Contact not found'}), 404     

@app.route('/api/contacts/<int:contact_id>', methods=['DELETE'])
def remove_contact(contact_id):
    global contacts
    contacts = [contact for contact in contacts if contact['id'] != contact_id] 
    return jsonify({'message': 'Contact deleted successfully'}), 200

if __name__ == '__main__':
      app.run(debug=True)