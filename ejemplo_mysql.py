import mysql.connector


def insert():
    miConexion = mysql.connector.connect(
        host='localhost', database='Personas', user='root', password='porter1986')
    miCursor = miConexion.cursor()
    miCursor.execute('''
                INSERT INTO alumnos values(32657232,'Federico','Tuñon Alves')
            ''')
    miConexion.commit()
    miCursor.close()
    miConexion.close()


def select():
    miConexion = mysql.connector.connect(
        host='localhost', database='Personas', user='root', password='porter1986')
    miCursor = miConexion.cursor()
    miCursor.execute('''
            SELECT * FROM alumnos
        ''')
    alumnos = miCursor.fetchall()
    print(alumnos)
    miCursor.close()
    miConexion.close()
