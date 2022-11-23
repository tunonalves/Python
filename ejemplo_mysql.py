import mysql.connector


def insert():
    miConexion = mysql.connector.connect(
        host='localhost', database='Personas', user='root', password='lalalla')
    miCursor = miConexion.cursor()
    miCursor.execute('''
                INSERT INTO alumnos values(9999999,'pablo','martinez')
            ''')
    miConexion.commit()
    miCursor.close()
    miConexion.close()


def select():
    miConexion = mysql.connector.connect(
        host='localhost', database='Personas', user='root', password='lalala')
    miCursor = miConexion.cursor()
    miCursor.execute('''
            SELECT * FROM alumnos
        ''')
    alumnos = miCursor.fetchall()
    print(alumnos)
    miCursor.close()
    miConexion.close()
