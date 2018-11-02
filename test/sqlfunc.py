import sqlite3 as sql
import os

filepath = os.path.dirname(os.path.abspath(__file__))
dbpath = os.path.join(filepath, 'words.db')
print(dbpath)


conn = sql.connect(dbpath)
cutsor = conn.cursor()
print(cutsor)
conn.close()
