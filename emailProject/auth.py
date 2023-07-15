from flask import request, render_template, Blueprint, redirect, jsonify

auth = Blueprint('auth', __name__)

@auth.route('/k-signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        age = request.form.get('age')
        fname = request.form.get('fname')
        lname = request.form.get('lname')

        print(request.form)

        if not email or not age or not fname or not lname:
            return jsonify({'success': False, 'message': 'All fields are required.'})

        return jsonify({'success': True, 'message': 'Form submitted successfully.'})

    if request.method == "GET":
        pass

    return render_template('signup.html')



# @auth.route('/login', methods=['GET', 'POST'])
# def login():
#     pass



