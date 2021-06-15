def capitales_mundo(*ciudades):
	for capital in ciudades:
		#for letra in capital:
			yield from capital
		


capitales_devueltas = capitales_mundo("Berlin","Roma","Buenos Aires","Bogota","Pekin","Madrid","Montevideo")

print(next(capitales_devueltas))
print(next(capitales_devueltas))
print(next(capitales_devueltas))