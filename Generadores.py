def numeros_pares(limite):
	num = 1
	numerosPares=[]
	while num<limite:
		numerosPares.append(num * 2)
		num = num + 1
	
	return numerosPares

print(numeros_pares(6))
