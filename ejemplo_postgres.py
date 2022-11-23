import psycopg2


def insert():
    miConexion = psycopg2.connect(host='localhost', database='Personas', user='postgres', password='lallala')
    miCursor = miConexion.cursor()
    miCursor.execute('''
            INSERT INTO alumnos values(999999,'pedro','sanchez')
        ''')
    miConexion.commit()
    miCursor.close()
    miConexion.close()

def select():
    miConexion = psycopg2.connect(host='localhost', database='Personas', user='postgres', password='lalalal')
    miCursor = miConexion.cursor()
    miCursor.execute('''
            SELECT * FROM alumnos
        ''')
    alumnos = miCursor.fetchall()
    print(alumnos)
    miCursor.close()
    miConexion.close()
