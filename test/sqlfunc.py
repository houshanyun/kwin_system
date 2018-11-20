import sqlite3 as sql
import os


class Sql_Create:
    filepath = os.path.dirname(os.path.abspath(__file__))
    dbpath = os.path.join(filepath, 'words.db')

    def __init__(self):
        self.conn = sql.connect(self.dbpath)


    def sql_add(self, en, tc):
        self.conn.execute(f"INSERT INTO 'word_table' VALUES('{en}', '{tc}')")


    def sql_edit(self):
        pass


    def sql_find(self):
        cur = self.conn.execute('select * from word_table')
        row = cur.fetchall()
        return row

    def sql_send(self):
        self.conn.commit()


    def sql_end(self):
        self.conn.close()
