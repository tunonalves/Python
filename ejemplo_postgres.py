import psycopg2


def insert():
    miConexion = psycopg2.connect(host='localhost', database='Personas', user='postgres', password='Porter1986')
    miCursor = miConexion.cursor()
    miCursor.execute('''
            INSERT INTO alumnos values(32657232,'Federico','Tuñon Alves')
        ''')
    miConexion.commit()
    miCursor.close()
    miConexion.close()

def select():
    miConexion = psycopg2.connect(host='localhost', database='Personas', user='postgres', password='Porter1986')
    miCursor = miConexion.cursor()
    miCursor.execute('''
            SELECT * FROM alumnos
        ''')
    alumnos = miCursor.fetchall()
    print(alumnos)
    miCursor.close()
    miConexion.close()