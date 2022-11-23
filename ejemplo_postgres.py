import psycopg2

miConexion = psycopg2.connect(host='localhost',database='Personas',user='postgres',password='Porter1986')
miCursor = miConexion.cursor()
miCursor.execute('''
        INSERT INTO alumnos values(32657232,'Federico','Tuñon Alves')
    ''')
miConexion.commit()
miCursor.close()
miConexion.close()
