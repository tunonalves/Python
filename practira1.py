import sqlite3

miConexion = sqlite3.connect("BBDD/nuevaBBDD")

miCursor = miConexion.cursor()
#miCursor.execute("Create Table Productos (ID INTEGER, NOMBRE VARCHAR(50), PRECIO INTEGER, SECCION VARCHAR(20))")
#miCursor.execute("INSERT INTO Productos(ID,NOMBRE,PRECIO,SECCION)values(1,'Camiseta',5000,'Moda')")
#miCursor.execute("INSERT INTO Productos values(1,'Camiseta',5000,'Moda')")

#muchosproductos = [
#    (2,"Patin",3000,"Deportes"),
#    (3,"Cenisero",200,"ceramica"),
#    (4,"pantalon",3420,"vestimenta")
#]

#miCursor.executemany("Insert into Productos values(?,?,?,?)",muchosproductos)
#miConexion.commit()

miCursor.execute("Select * from Productos")

muchos = miCursor.fetchall()

print(muchos)

miCursor.close()

miConexion.close()