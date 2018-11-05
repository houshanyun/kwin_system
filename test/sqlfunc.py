import sqlite3 as sql
import os
import pandas as pd

filepath = os.path.dirname(os.path.abspath(__file__))
dbpath = os.path.join(filepath, 'words.db')


conn = sql.connect(dbpath)
cutsor = conn.cursor()
a = conn.execute('select * from wordsone')
data = a.fetchall()
print(data)
ds = pd.DataFrame(data)

conn.close()
