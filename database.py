import sqlite3

def create_connection():
    conn = sqlite3.connect('ministra_con_amor.db')
    return conn

def create_table():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS hermanos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            direccion TEXT,
            telefono TEXT,
            correo TEXT,
            necesidades TEXT
        )
    ''')
    conn.commit()
    conn.close()

def add_hermano(nombre, direccion, telefono, correo, necesidades):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO hermanos (nombre, direccion, telefono, correo, necesidades)
        VALUES (?, ?, ?, ?, ?)
    ''', (nombre, direccion, telefono, correo, necesidades))
    conn.commit()
    conn.close()

def get_hermanos():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM hermanos')
    hermanos = cursor.fetchall()
    conn.close()
    return hermanos

# Inicializar la base de datos
create_table()