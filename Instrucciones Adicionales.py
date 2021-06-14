nombre="Federico Tuñon Alves"

print(len(nombre))

contador = 0

for i in nombre:
	if i == " ":
		continue # Continua sin contar los espacios en blanco
	contador+=1
print(contador)


for i in nombre:
	pass  # pasa el bucle sin hacer nada


email = input("Email: ")

for i in email:
	if i == "@":
		arroba = True
		break
else:
	arroba = False

print(arroba)