import sqlite3
from datetime import datetime


DATABASE = 'notevix.db'

def init_db():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            feature TEXT NOT NULL,
            input_text TEXT NOT NULL,
            result TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    conn.commit()
    conn.close()

def save_result(feature, input_text, result):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    
    cursor.execute('''
        INSERT INTO history (feature, input_text, result)
        VALUES (?, ?, ?)
    ''', (feature, input_text, result))
    
    conn.commit()
    conn.close()


def get_history():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM history ORDER BY created_at DESC LIMIT 20"
    )
    rows = cursor.fetchall()
    conn.close()
    return rows



def get_history_by_feature(feature):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM history WHERE feature = ? ORDER BY created_at DESC",
        (feature,)
    )
    rows = cursor.fetchall()
    conn.close()
    return rows


