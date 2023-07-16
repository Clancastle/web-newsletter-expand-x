from flask import Blueprint, render_template, request, jsonify
import json

views = Blueprint('views', __name__)

@views.route('/', methods=['GET'])
def home():
    return render_template('mainpage.html')

@views.route('/newsletter/')
def newsletter():
    return render_template('newspast.html')