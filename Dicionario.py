lascapitales={"Argentina":"Buenos Aires","España":"Madrid","Francia":"Toulousse","Reino Unido":"Londres"}

lascapitales["Colombia"]="Bogota"

lascapitales["Francia"]="Paris"

print(lascapitales)

del lascapitales["Reino Unido"]

print(lascapitales)

datos={"España":"Madrid",23:"M. Jordan","Mosquetero":3}

print(datos)


claveCapitales=["España","Argentina","Italia","Colombia"]
capitalesMundo={claveCapitales[0]:"Madrid",claveCapitales[1]:"Buenos Aires",claveCapitales[2]:"Roma",claveCapitales[3]:"Bogota"}

print(capitalesMundo)

print(capitalesMundo.keys())
print(capitalesMundo.values())
print(len(capitalesMundo))

#diccionario anidado con otro diccionario

datosJordan={23:"Jordan","Nombre":"Michael","Equipo":"C Bulls","Anillos":{"Temporadas":[1991,1992,1993,1996,1997,1998]}}

print(datosJordan)

