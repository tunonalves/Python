class Persona():

	def __init__(self,nombre,apellido,edad):
	    self.nombre=nombre
	    self.apellido=apellido
	    self.edad=edad
	
	def getDatosPersonales(self):
		return "Nombre: "+self.nombre+" Apellido: "+self.apellido+" Edad: "+str(self.edad)
	
	def Habla(self):
		return "Estoy hablando"
	
	def Piensa(self):
		return "Estoy Pensando"

	def Camina(self):
		return "Estoy Caminando"
	
	def Come(self):
		return "Estoy Comiendo"
	
class Estudiante(Persona):
	
	def Estudia(self):
		return "Estoy Estudiando"
	

Persona1 = Persona("Federico","Tuñon Alves",35)
Estudiante1 = Estudiante("Pedro","Lopez",40)


print(Persona1.getDatosPersonales())
