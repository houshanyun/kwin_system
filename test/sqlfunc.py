import sqlite3 as sql
import os


class Sql_Create:
    filepath = os.path.dirname(os.path.abspath(__file__))
    dbpath = os.path.join(filepath, 'words.db')

    def __init__(self):
        self.conn = sql.connect(self.dbpath)


    def sql_addval(self, en, tc):
        self.conn.execute(f"INSERT INTO 'word_table' VALUES('{en}', '{tc}')")

    def sql_alter(self, col_name, typ='INTEGER'):
        self.conn.execute(f'ALTER TABLE word_table ADD COLUMN {col_name} {typ}')


    def sql_edit(self, count, num):
        self.conn.execute(f'UPDATE word_table SET ER = {count} WHERE ID = {num}')


    def sql_find(self):
        cur = self.conn.execute('SELECT * FROM word_table')
        row = cur.fetchall()
        return row

    def sql_send(self):
        self.conn.commit()


    def sql_end(self):
        self.conn.close()
