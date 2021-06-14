capitales={"Argentina":"Buenos Aires","España":"Madrid","Italia":"Roma","EEUU":"Washinton","Reino Unido":"Londres"}

for clave in capitales:
	valor = capitales[clave]
	print(clave)
	print(valor)

print(capitales.items())


for clave, valor in capitales.items():
	print(clave + "  ->  " + valor)

