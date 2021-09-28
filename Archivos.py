from io import open

archivo_externo = open("primerArchivo.txt","r+")

#archivo_externo.write("\n Bienvenidos a los archivos externos")

#informacion_lineas = archivo_externo.readlines();

print(archivo_externo.read())
archivo_externo.seek(0)
print(archivo_externo.read(6))
archivo_externo.seek(len(archivo_externo.read())/2)
print(archivo_externo.read())



archivo_externo.close()

