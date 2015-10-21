import sqlite3

connect = sqlite3.connect('db1.db')
DBcursor = connect.cursor()

DBcursor.execute("CREATE TABLE users(id INTEGER PRIMARY KEY, name TEXT, memberStatus BOOLEAN)")
DBcursor.execute("CREATE TABLE carsOnSale(id INTEGER PRIMARY KEY, brand TEXT)")
 