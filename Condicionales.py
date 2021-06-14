def evaluacion(nota):
	valoracion = "NULL"
	if(nota >= 5) and (nota <= 7):
		valoracion= "Suspenso"
	elif(nota>=8) and (nota <= 10):
		valoracion = "Aprobado"
	elif(nota>10):
		valoracion = "Nota Incorrecta"
	else:
		valoracion = "Desaprobado"
	return valoracion

nota_alumno=input("Introduce la nota: ")

print(evaluacion(int(nota_alumno)))


print("Obtencion carnet de conducir")

edad = int(input("Introduce tu edad, por favor: "))

def validacion(edad):
	if (18 <= edad <= 90):
		print("Puedes intentar obtener el carnet")
	else:
		print("Lo siento. No cumples con la edad necesaria")

validacion(edad)

lenguajes=["Java","Python","PHP","C#","Visual Basic"]

if "SQL" not in lenguajes:
	print("Falta el lenguaje")
else:
	print("Esta en la lista")
