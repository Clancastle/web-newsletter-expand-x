import os
from flask import Flask, Blueprint, jsonify, request

path_cwd = os.path.dirname(os.path.realpath(__file__))
path_templates = os.path.join(path_cwd, "templates")
path_static = os.path.join(path_cwd, "static")

Func = Blueprint('func', __name__, static_folder=path_static, template_folder=path_templates)

@Func.route('/func', methods=['POST'])
def func():
    dataGet = request.get_json(force=True)

    # Process the received data
    email = dataGet.get('email')
    fname = dataGet.get('fname')
    lname = dataGet.get('lname')
    age = dataGet.get('age')

    # Perform any necessary actions with the data

    dataReply = {'backend_data': 'some_data'}
    return jsonify(dataReply)
