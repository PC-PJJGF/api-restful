import sqlite3

# Conectar a la base de datos (se creará si no existe)
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Crear una tabla si no existe
cursor.execute('''
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS productos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    precio REAL NOT NULL,
    stock INTEGER NOT NULL
)
''')

# Insertar datos de ejemplo
cursor.execute("INSERT INTO usuarios (nombre, email, password) VALUES (?, ?, ?)", ("Carlos", "carlos@example.com", "1234"))
cursor.execute("INSERT INTO usuarios (nombre, email, password) VALUES (?, ?, ?)", ("Maria", "maria@example.com", "1234"))
cursor.execute("INSERT INTO productos (nombre, precio, stock) VALUES (?, ?, ?)", ("Producto 1", 10.0, 20))
cursor.execute("INSERT INTO productos (nombre, precio, stock) VALUES (?, ?, ?)", ("Producto 2", 15.0, 30))
cursor.execute("INSERT INTO productos (nombre, precio, stock) VALUES (?, ?, ?)", ("Producto 3", 20.0, 15))

cursor.execute("INSERT INTO productos (nombre, precio, stock) VALUES (?, ?, ?)", ("Producto 4", 25.0, 10))
cursor.execute("INSERT INTO productos (nombre, precio, stock) VALUES (?, ?, ?)", ("Producto 5", 30.0, 5))
cursor.execute("INSERT INTO productos (nombre, precio, stock) VALUES (?, ?, ?)", ("Producto 6", 35.0, 0))

# Guardar los cambios y cerrar la conexión
conn.commit()
conn.close()

print("Datos insertados correctamente.")
