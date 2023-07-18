from flask import request, render_template, Blueprint, redirect, jsonify
import re
import sqlite3

auth = Blueprint('auth', __name__)
k = "k string"
@auth.route('/k-signup', methods=['GET', 'POST'])
def signup():
    conn = sqlite3.connect('non_sensitive_data.db')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS user_data (first_name VARCHAR(20), last_name VARCHAR(25), age INT, email VARCHAR(249))')

    e_re = re.compile(r"([-!#-'*+/-9=?A-Z^-~]+(\.[-!#-'*+/-9=?A-Z^-~]+)*|\"([]!#-[^-~ \t]|(\\[\t -~]))+\")@([-!#-'*+/-9=?A-Z^-~]+(\.[-!#-'*+/-9=?A-Z^-~]+)*|\[[\t -Z^-~]*])")
    if request.method == 'POST':

        un_email = request.form.get('email')
        un_age = request.form.get('age')
        un_fname = request.form.get('fname')
        un_lname = request.form.get('lname')
        # print(re.fullmatch(e_re, un_email))
        validation_passed = True
        try:
            if len(un_fname) <= 25 and len(un_fname) >= 3 and not re.search(r'[\d\W]', un_fname):
                print('validation: first name passed')
            else:
                print('validation: first name failed')
                un_fname = None
                validation_passed = False

            if len(un_lname) <= 25 and len(un_lname) >= 3 and not re.search(r'[\d\W]', un_lname):
                print('validation: last name passed' )
            else:
                print('validation: last name failed')
                un_lname = None
                validation_passed = False

            if un_age.isdigit() and 10 < int(un_age) < 100: #re.match(r'^\d+$', un_age
                print('validation: age passed')
            else:
                print('validation: age failed')
                un_age = None
                validation_passed = False


            if re.match(e_re, un_email) and len(un_email) < 500:
                print('validation: email passed')
            else:
                print('validation: email failed')
                un_email = None
                validation_passed = False


            cursor.execute('INSERT INTO user_data (first_name, last_name, age, email) VALUES (?, ?, ?, ?)', (un_fname, un_lname, un_age, un_email))

            conn.commit()

            cursor.execute('SELECT * FROM user_data ')
            data = cursor.fetchall()
            for i in data:
                print(i)
            print(un_fname, un_lname, un_age, un_email)
        except Exception as e:
            print(str(e))

        cursor.close()
        conn.close()

        # print(request.form)

        # if not email or not age or not fname or not lname:
        #     return jsonify({'success': False, 'message': 'All fields are required.'})
        #
        # return jsonify({'success': True, 'message': 'Form submitted successfully.'})
        if validation_passed:
            return redirect('/')
        else:
            return redirect('k-signup')

    if request.method == "GET":
        pass

    return render_template('signup.html')

@auth.route('/unsubscribe', methods=['GET', 'POST'])
def unsubscribe():
    return render_template('unsubscribe.html')


# @auth.route('/login', methods=['GET', 'POST'])
# def login():
#     pass



