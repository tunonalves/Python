class Persona():

	datos_array=[]

	def __init__(self, *datos): #Es tupla en el constructor
	    for dato in datos:
		    self.datos_array.append(dato)
	    self.getDatos(self.datos_array) #devuelve los datos


	def getDatos(self,info):
		for dato in info:
			print(dato)


	def __str__(self): #pasa a string la info del objeto
		return "Datos: \n"+str(self.datos_array[0]) +"\n"+ str(self.datos_array[1]) + "\n" + str(self.datos_array[2])


p1 = Persona("Federico","Tuñon",34,"La Tecla")

#print(p1)

