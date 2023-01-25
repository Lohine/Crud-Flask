from flask import Flask, jsonify, request, render_template
app = Flask(__name__)

contacts = [{'id': 1, 'name': 'John Doe', 
'phone': '555-555-5555'}]

# GET request to retrieve all contacts and method get
@app.route('/contacts', methods=['GET'])
def get_contacts():
    return {'contacts': contacts}


# GET request to retrieve one contacts
@app.route('/contacts/<int:id>', methods=['get'])
def get_contact(id):
    return {'contact': contacts [int(id)-1] }
 
    
# POST request to add a new contact with data of the new contact on a json file
@app.route('/contacts', methods=['POST'])
def add_contact():
    #id is created here 
    contact = {'id': len(contacts) + 1, 'name': request.json ['name'], 'phone': request.json ['phone'] }
    contacts.append(contact)
    return {'contact' : contact}

# PUT request to update a contact
@app.route('/contacts/<int:id>', methods=['PUT'])
def update_contact(id):
    
    if id > len(contacts):
        return{'message': 'Contact not found'}
    
    contact = {'id': len(contacts) + 1, 'name': request.json ['name'], 'phone': request.json ['phone'] }
    contacts[id-1] = contact

    return {'contact': contact}



# DELETE request to delete a contact
@app.route('/contacts/<int:id>', methods=['DELETE'])
def delete_contact(id):
    if id > len(contacts):
        return {'message': 'Contact not found'}
    contacts.pop[id-1]
    return{'message': 'Contact deleted'}


app.run(debug=True)