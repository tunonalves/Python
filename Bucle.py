contador=0

while contador < 100:
	print(contador)
	contador = contador + 1

print("Fin")


edad = int(input("Indroduce tu edad: "))
while edad < 0:
	print("Has introducido una edad negativa no validad")
	edad=int(input("Introduce tu edad: "))
print("Gracias")
print("Edad = "+str(edad))

