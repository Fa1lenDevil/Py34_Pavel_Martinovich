import sqlite3


database = sqlite3.connect('../database.db')

with open('posts.sql') as f:
    database.executescript(f.read())

cur = database.cursor()

cur.execute("INSERT INTO posts (username, password) VALUES (?, ?)", ('Pushkin228', '*************'))
cur.execute("INSERT INTO posts (username, password) VALUES (?, ?)", ('Slavyanin322', '******************'))

database.commit()
database.close()