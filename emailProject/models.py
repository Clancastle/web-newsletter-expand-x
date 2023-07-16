import sqlite3
from flask import Flask, render_template

app = Flask(__name__)

@app.before_request
def takeData():
    connect = sqlite3.connect('emails.db')
    cursor = connect.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS email_list (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        email TEXT NOT NULL
                    )''')

    fet = cursor.fetchall()

    cursor.close()
    connect.close()


if __name__ == '__main__':
    app.run()
