import math

def calculo_raiz_cuadrada(numero):
	if numero < 0:
		raise ValueError ("Error numero negativo") #Lanza forzozamente una exception
	else:
		return math.sqrt(numero)

numeroUsuario = (int(input("Numero: ")))

try:
	print(calculo_raiz_cuadrada(numeroUsuario))
except ValueError:
	print("ERROR")

print("FIN PROGRAMA")
