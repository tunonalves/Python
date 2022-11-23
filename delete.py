import sqlite3

miConexion = sqlite3.connect("BBDD/gestionpedidos")
miCursor = miConexion.cursor()
miCursor.execute("Delete from Productos where CODIGO_ART = 'AR02'")
miConexion.commit()
miCursor.close()
miConexion.close()