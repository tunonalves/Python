def evaluacion(nota):
	valoracion = "NULL"
	if(nota >= 5 and nota <= 7):
		valoracion= "Suspenso"
	elif(nota>=8):
		valoracion = "Aprobado"
	else:
		valoracion = "Desaprobado"
	return valoracion

nota_alumno=input("Introduce la nota: ")

print(evaluacion(int(nota_alumno)))
