import sqlite3
from note import Note

class Database:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS notes
                                (id INTEGER PRIMARY KEY, title TEXT, content TEXT, deadline TEXT)''')

    def add(self, title, content, deadline):
        self.cursor.execute('INSERT INTO notes (title, content, deadline) VALUES (?, ?, ?)', (title, content, deadline))
        self.conn.commit()

    def get_all(self):
        self.cursor.execute('SELECT * FROM notes')
        return [Note(id, title, content, deadline) for id, title, content, deadline in self.cursor.fetchall()]

    def update(self, id, title, content, deadline):
        self.cursor.execute('UPDATE notes SET title = ?, content = ?, deadline = ? WHERE id = ?', (title, content, deadline, id))
        self.conn.commit()

    def delete(self, id):
        self.cursor.execute('DELETE FROM notes WHERE id = ?', (id,))
        self.conn.commit()

    def close(self):
        self.conn.close()
