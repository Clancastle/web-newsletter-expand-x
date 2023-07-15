from flask import request, render_template, Blueprint

auth = Blueprint('auth', __name__)

@auth.route('/k-signup', methods=['GET', 'POST'])
def signup():
    t = request.method
    data = request.form
    print(t, data)
    return render_template('signup.html')



# @auth.route('/login', methods=['GET', 'POST'])
# def login():
#     pass



