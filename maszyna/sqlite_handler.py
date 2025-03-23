import os
import sqlite3
import config

def create_table(headers):
    conn = sqlite3.connect(config.SQLITE_DB_PATH)
    c = conn.cursor()
    c.execute(f"""CREATE TABLE IF NOT EXISTS {config.TABLE_NAME} (
  [Id] INTEGER NOT NULL
, [a] NUMERIC NOT NULL
, [b] NUMERIC NOT NULL
, [c] NUMERIC NOT NULL
, [d] NUMERIC NOT NULL
, [e] NUMERIC NOT NULL
, [f] NUMERIC NOT NULL
, [g] NUMERIC NOT NULL
, [h] NUMERIC NOT NULL
, [timestamp] TIMESTAMP DEFAULT CURRENT_TIMESTAMP
, CONSTRAINT [PK_dane] PRIMARY KEY ([Id])
);""")
    conn.commit()
    conn.close()

def insert_data(headers,data):
    conn = sqlite3.connect(config.SQLITE_DB_PATH)
    cursor = conn.cursor()
    placeholders = ', '.join(["?" for _ in headers])
    cursor.executemany(f"INSERT INTO {config.TABLE_NAME}(a, b, c, d, e, f, g, h) VALUES ({placeholders})",data)
    
    conn.commit()
    conn.close()
    
def read_data(table_name):
    conn = sqlite3.connect(config.SQLITE_DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute(f"SELECT * FROM {table_name}")
    data = cursor.fetchall()
    
    cursor.execute(f"PRAGMA table_info({table_name})")
    headers = cursor.fetchall()
    return headers, data
