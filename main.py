import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)")

name = input("Enter a name: ")
cursor.execute("INSERT INTO users (name) VALUES (?)", (name,))
conn.commit()