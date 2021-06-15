import sys
def divide():
	intentos = 0
	while True:
		try:
			op1=(float(input("Numero UNO: ")))
			op2=(float(input("Numero DOS: ")))
			print("Resultado: "+str(op1/op2))
			break
		except ZeroDivisionError:
			print("Divicion por Zero")
			intentos += 1
		except ValueError:
			print("Valores Erroneos")
			intentos += 1
		if (intentos == 3):
			sys.exit()
		

divide()
print("FIN")