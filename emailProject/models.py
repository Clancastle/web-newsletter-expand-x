import sqlite3
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


conn = sqlite3.connect('non_sensitive_data.db')
cursor = conn.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTS user_data (first_name VARCHAR(20), last_name VARCHAR(25), age INT, email VARCHAR(80))')
