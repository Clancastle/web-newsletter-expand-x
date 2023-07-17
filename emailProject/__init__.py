from flask import Flask, render_template
import sqlite3
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'den'


    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app

app = create_app()


if __name__ == '__main__':
    app.run()

