class Persona():
	nombre = ""
	apellido = ""
	edad = 0
	genero = ""

	def __init__(self,nombre,apellido,edad,genero):
		self.nombre = nombre
		self.apellido = apellido
		self.edad = edad
		self.genero = genero

	def habla(self):
		return "La persona que se llama " + self.nombre + " esta hablando"
	def camina(self):
		return "La persona que se llama " + self.nombre + " esta caminando"
	def getdatos(self):
		return "Nombre: "+self.nombre+" Apellido: "+self.apellido + \
			" Edad: "+str(self.edad) + " Genero: " + self.genero

mipersona = Persona("Juan","Perez",34,"Varon")


print(mipersona.getdatos())
