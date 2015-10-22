import sqlite3

connect = sqlite3.connect('db1.db')
DBcursor = connect.cursor()

DBcursor.execute("CREATE TABLE users(id INTEGER PRIMARY KEY, name TEXT)")


DBcursor.execute("INSERT INTO users VALUES(1,'heikern')")
DBcursor.execute("INSERT INTO users VALUES(2,'heimern')")
connect.commit()
 