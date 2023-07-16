from flask import Flask, render_template
import sqlite3
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'den'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///emails.db'  # Specify the database URI


    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app


app = create_app()

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
    db = SQLAlchemy(app)  # Initialize SQLAlchemy with the app
    db.create_all()  # Create all tables based on the defined models

if __name__ == '__main__':
    create_table()
    app.run()
