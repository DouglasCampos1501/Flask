from flask import Flask, jsonify, request, render_template, Response
crud = Flask(__name__)

contacts = [{'id': 1, 'name': 'John Doe', 'phone': '555-555-5555'}]

# route template
@crud.route('/contact',methods=['GET'])
def contact():
    return render_template('crud.html')


@crud.route('/all_contact',methods=['POST'])
def all_contact_post():
    name = request.json['name']
    phone = request.json['phone']
    id = request.json['id']
    contact = {'id':id,'name':name,'phone':phone}
    contacts.append(contact)
    return jsonify(contact)


# # GET request to retrieve one contacts
@crud.route('/contacts/<str:"name">', methods=['get'])
def get_contact(id):
    return {'contact': ''}











# # GET request to retrieve all contacts
# @crud.route('/contacts', methods=['GET'])
# def get_contacts():
#     return {'contacts': ''}

# # GET request to retrieve one contacts
# @crud.route('/contacts/<int:id>', methods=['get'])
# def get_contact(id):
#     return {'contact': ''}

# # POST request to add a new contact with data of the new contact on a json file
# @crud.route('/contacts', methods=['POST'])
# def add_contact():
#     #id is created here 
#     return {'contact': ''}

# # PUT request to update a contact
# @crud.route('/contacts/<int:id>', methods=['PUT'])
# def update_contact(id):
#     return {'contact': ''}

# # DELETE request to delete a contact
# @crud.route('/contacts/<int:id>', methods=['DELETE'])
# def delete_contact(id):
#     return {'message': ''}


crud.run(debug=True)