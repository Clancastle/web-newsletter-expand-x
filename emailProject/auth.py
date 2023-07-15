from flask import request, render_template, Blueprint, redirect

auth = Blueprint('auth', __name__)

@auth.route('/k-signup', methods=['GET', 'POST'])
def signup():

    # data = request.get_json()
    # email = data.get('email')
    # age = data.get('age')
    # fname = data.get('fname')
    # lname = data.get('lname')

    if request.method == 'POST':
        print(request.form)

    if request.method == "GET":
        pass

    return render_template('signup.html')



# @auth.route('/login', methods=['GET', 'POST'])
# def login():
#     pass



