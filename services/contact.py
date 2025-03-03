from flask import Blueprint, request, jsonify
from model.contact import Contact 

contacts= Blueprint('contacts',__name__)

@contacts.route('/contactos/v1', methods=['GET'])
def getMensaje():
    result={}
    result["data"]='flask-crud-backend'
    return jsonify(result)

@contacts.route('/contactos/v1/listar', methods=['GET'])
def getContactos():
    result={}
    contactos=Contact.query.all()
    result["data"]=contactos
    result["stauts_cod"]=200
    result["msg"]="Se recupero los contactos sin incovenientes"
    return jsonify(result)
