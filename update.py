import sqlite3

miConexion = sqlite3.connect("BBDD/gestionpedidos")
miCursor = miConexion.cursor()
miCursor.execute("Update Productos Set PRECIO=35 where CODIGO_ART = 'AR02'")
miConexion.commit()
miCursor.close()
miConexion.close()