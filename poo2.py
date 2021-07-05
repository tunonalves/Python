class Persona():
	__nombre = ""
	__apellido = ""
	__edad = 0
	__genero = ""

	def __init__(self,nombre,apellido,genero):
		self.__nombre = nombre
		self.__apellido = apellido
		
		self.__genero = genero
	
	def setEdad(self,edad):
		if(edad < 0 or edad >100):
			return "Error en la edad"
		else:
			self.__edad = edad
			return self.__edad


	def habla(self):
		return "La persona que se llama " + self.__nombre + " esta hablando"
	def camina(self):
		return "La persona que se llama " + self.__nombre + " esta caminando"
	def getdatos(self):
		return "Nombre: "+self.__nombre+" Apellido: "+self.__apellido + \
			" Edad: "+str(self.__edad) + " Genero: " + self.__genero


	




mipersona = Persona("Juan","Perez","Varon")

mipersona.setEdad(67)

print(mipersona.getdatos())

mipersona.__nombre="Federico" #No funciona por el encapsulamiento

print(mipersona.getdatos())

