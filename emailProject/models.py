import sqlite3
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


conn = sqlite3.connect('non_sensitive_data.db')
cursor = conn.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTS user_data (first_name VARCHAR(20), last_name VARCHAR(25), age INT, email VARCHAR(249))')
# conn.commit()
# cursor.execute('SELECT * FROM user_data')
# data = cursor.fetchall()
# print(data)
# for i in data:
#     print(i)

cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
tables = cursor.fetchall()

# Iterate over tables
for table in tables:
    table_name = table[0]
    print(f"Table: {table_name}")

    # Retrieve column names for each table
    cursor.execute(f"PRAGMA table_info('{table_name}')")
    columns = cursor.fetchall()

    # Iterate over columns
    for column in columns:
        column_name = column[1]
        print(f"  Column: {column_name}")

# Close the connection
cursor.close()
conn.close()
