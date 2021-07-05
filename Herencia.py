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
	
	def __init__(self, nombre, apellido, edad, escuela):
	    super().__init__(nombre, apellido, edad)
	    self.escuela=escuela

	def Estudia(self):
		return "Estoy Estudiando"
	
	def getDatosPersonales(self):
	    return super().getDatosPersonales() + " Escuela: "+self.escuela





Persona1 = Persona("Federico","Tuñon Alves",35)
Estudiante1 = Estudiante("Pedro","Lopez",40,"San Javier")


print(Persona1.getDatosPersonales())
print(Estudiante1.getDatosPersonales())
