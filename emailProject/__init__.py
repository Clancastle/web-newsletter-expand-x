from flask import Flask, render_template
import sqlite3
from flask_login import LoginManager

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'den'

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app

app = Flask(__name__)
@app.route('/k-signup')
def takeData():
    connect = sqlite3.connect('emails.db')
    cursor = connect.cursor()

    fet = cursor.fetchall()

    cursor.close()
    connect.close()
    print(fet)
    return render_template('signup.html')

def create_table():
    connect = sqlite3.connect('emails.db')
    cursor = connect.cursor()

    # Create the email_list table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS email_list (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT NOT NULL
        )
    ''')

    connect.commit()
    cursor.close()
    connect.close()

if __name__ == '__main__':
    create_table()
    app.run()
