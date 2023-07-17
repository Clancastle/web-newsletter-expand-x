import sqlite3
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
@app.route('/')
def create_table():
    conn = sqlite3.connect('emails.db')
    cursor = conn.cursor()

    cursor.execute('CREATE TABLE IF NOT EXISTS email_table (emails VARCHAR(100))')

    cursor.close()
    conn.close()

    return 'Created successfully'
