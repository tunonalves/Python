import sqlite3

def uno():
    miConexion = sqlite3.connect("BBDD/gestionpedidos")
    miCursor = miConexion.cursor()
    miCursor.execute('''
        Create Table Productos (
            CODIGO_ART VARCHAR(4) PRIMARY KEY UNIQUE,
            NOMBRE_ART VARCHAR(40),
            PRECIO FLOAT,
            SECCION VARCHAR(20)
        )
    ''')
    miConexion.commit()
    miCursor.close()
    miConexion.close()

def dos():
    miConexion = sqlite3.connect("BBDD/gestionpedidos")
    miCursor = miConexion.cursor()
    miCursor.execute('''
        Create Table Productos (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            NOMBRE_ART VARCHAR(40),
            PRECIO FLOAT,
            SECCION VARCHAR(20)
        )
    ''')
    miConexion.commit()
    miCursor.close()
    miConexion.close()