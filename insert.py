import sqlite3

miConexion = sqlite3.connect("BBDD/gestionpedidos")
miCursor = miConexion.cursor()
Productos = [
    ("AR01","Camiseta",34,"moda"),
    ("AR02","Pantalon",43,"moda"),
    ("AR03","Campera",53,"moda"),
    ("AR04","Medias",12,"moda")
]
miCursor.executemany("Insert Into Productos values(?,?,?,?)",Productos)
miConexion.commit()
miCursor.close()
miConexion.close()