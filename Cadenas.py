

nUsuario = input("Usuario: ")

print("El Usuario es: ", nUsuario.upper())
print("El Usuario es: ", nUsuario.lower())
print("El Usuario es: ", nUsuario.capitalize())

edad = input("Edad: ")
while(edad.isdigit() == False):
	print("ERROR")
	edad = input("Edad: ")

if(int(edad)<18):
	print("Edad: ",str(edad))
else:
	print("Edad: ",str(edad))

