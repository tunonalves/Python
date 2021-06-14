import math

contador=0
while contador < 100:
	print(contador)
	contador = contador + 1
print("Fin")
print("-------------------")
edad = int(input("Indroduce tu edad: "))
while edad < 0:
	print("Has introducido una edad negativa no validad")
	edad=int(input("Introduce tu edad: "))
print("Gracias")
print("Edad = "+str(edad))
print("-------------------")
print("Raiz cuadrada")
numero=int(input("Numero: "))
intentos = 1
while (numero < 0):
	print("El numero no puede ser negativo")
	numero=int(input("Numero: "))
	intentos = intentos + 1
	if (intentos == 3):
		break
print("-------------------")
print(math.isqrt(numero))