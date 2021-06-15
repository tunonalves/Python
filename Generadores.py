def numeros_pares(limite):
	num = 1
	numerosPares=[]
	while num<limite:
		numerosPares.append(num * 2)
		num = num + 1
	
	return numerosPares

print(numeros_pares(6))


def numeros_pares2(limite):
	num = 1
	while num<limite:
		yield num * 2
		num = num + 1
		
numeros = numeros_pares2(6)
for i in numeros:
	print(i)
