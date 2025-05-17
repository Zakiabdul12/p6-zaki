import sqlite3
import os
from dotenv import load_dotenv

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL", "database.db")

def get_db_connection():
    conn = sqlite3.connect(DATABASE_URL)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    try:
        with open('schema.sql') as f:
            conn.executescript(f.read())
        conn.commit()
        print("Database initialized.")
    except Exception as e:
        print(f"Error initializing database: {e}")
    finally:
        conn.close()

def get_user_by_username(username):
    conn = get_db_connection()
    try:
        user = conn.execute('SELECT * FROM users WHERE username = ?', (username,)).fetchone()
        return user
    finally:
        conn.close()

def get_all_mahasiswa():
    conn = get_db_connection()
    try:
        mahasiswa_list = conn.execute('SELECT * FROM mahasiswa ORDER BY nama').fetchall()
        return mahasiswa_list
    finally:
        conn.close()

def get_mahasiswa_by_id(mahasiswa_id):
    conn = get_db_connection()
    try:
        mahasiswa = conn.execute('SELECT * FROM mahasiswa WHERE id = ?', (mahasiswa_id,)).fetchone()
        return mahasiswa
    finally:
        conn.close()

def add_mahasiswa_db(nama, nim):
    conn = get_db_connection()
    try:
        conn.execute('INSERT INTO mahasiswa (nama, nim) VALUES (?, ?)', (nama, nim))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()

def update_mahasiswa_db(mahasiswa_id, nama, nim):
    conn = get_db_connection()
    try:
        conn.execute('UPDATE mahasiswa SET nama = ?, nim = ? WHERE id = ?', (nama, nim, mahasiswa_id))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()

def delete_mahasiswa_db(mahasiswa_id):
    conn = get_db_connection()
    try:
        conn.execute('DELETE FROM mahasiswa WHERE id = ?', (mahasiswa_id,))
        conn.commit()
    finally:
        conn.close()

def count_mahasiswa():
    conn = get_db_connection()
    try:
        count = conn.execute("SELECT COUNT(id) FROM mahasiswa").fetchone()[0]
        return count
    finally:
        conn.close()

if not os.path.exists(DATABASE_URL):
    init_db()
else:
    conn = get_db_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='users';")
        if cursor.fetchone() is None:
            init_db()
    finally:
        conn.close()