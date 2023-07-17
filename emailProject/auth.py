from flask import request, render_template, Blueprint, redirect, jsonify
import re
import sqlite3

auth = Blueprint('auth', __name__)
k = "k string"
@auth.route('/k-signup', methods=['GET', 'POST'])
def signup():
    e_re = re.compile(r"([-!#-'*+/-9=?A-Z^-~]+(\.[-!#-'*+/-9=?A-Z^-~]+)*|\"([]!#-[^-~ \t]|(\\[\t -~]))+\")@([-!#-'*+/-9=?A-Z^-~]+(\.[-!#-'*+/-9=?A-Z^-~]+)*|\[[\t -Z^-~]*])")
    if request.method == 'POST':
        def Validate():
            un_email = request.form.get('email')
            un_age = request.form.get('age')
            un_fname = request.form.get('fname')
            un_lname = request.form.get('lname')
            # print(re.fullmatch(e_re, un_email))
            try:
                if len(un_fname) <= 25 and len(un_fname) >= 3 and not re.search(r'[\d\W]', un_fname):
                    print('validation: first name passed')
                    fname = un_fname
                else:
                    print('validation: first name failed')
                    fname = None

                if len(un_lname) <= 25 and len(un_lname) >= 3 and not re.search(r'[\d\W]', un_lname):
                    print('validation: last name passed' )
                    lname = un_lname
                else:
                    print('validation: last name failed')
                    lname = None

                if un_age.isdigit() and 10 < int(un_age) < 100: #re.match(r'^\d+$', un_age
                    print('validation: age passed')
                    age = un_age
                else:
                    print('validation: age failed')
                    age = None

                if re.match(e_re, un_email) and len(un_email) < 100:
                    print('validation: email passed')
                    vemail = un_email
                else:
                    print('validation: email failed')
                    vemail = None
                print(k)
                print(fname, lname, age, vemail)
            except Exception as e:
                print(str(e))
        Validate()

        print(request.form)

        # if not email or not age or not fname or not lname:
        #     return jsonify({'success': False, 'message': 'All fields are required.'})
        #
        # return jsonify({'success': True, 'message': 'Form submitted successfully.'})

    if request.method == "GET":
        pass

    return render_template('signup.html')



# @auth.route('/login', methods=['GET', 'POST'])
# def login():
#     pass



