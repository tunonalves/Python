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
	    Persona.__init__(self,nombre, apellido, edad)
	    self.escuela=escuela

	def Estudia(self):
		return "Estoy Estudiando"
	
	def getDatosPersonales(self):
	    return super().getDatosPersonales() + " Escuela: "+self.escuela


class Trabajador(Persona):
	
	def __init__(self, nombre, apellido, edad, Empresa):
	    Persona.__init__(self,nombre, apellido, edad)
	    self.empresa=Empresa
	
	def Trabaja(self):
		return "Estoy Trabajando"

	def getDatosPersonales(self):
	    return super().getDatosPersonales() + " Empresa: "+self.empresa
	    


class Director(Trabajador,Estudiante): #Herencia Multiple

	def __init__(self, nombre, apellido, edad, Empresa, Escuela,bonus):
	    Trabajador.__init__(self,nombre, apellido, edad, Empresa)
	    Estudiante.__init__(self,nombre, apellido, edad, Escuela)
	    self.bonus=bonus

	def getDatosPersonales(self):
	    return super().getDatosPersonales() + " Bonus: " + str(self.bonus)

	def Dirige(self):
		return "Estoy Dirigiendo"








Persona1 = Persona("Federico","Tuñon Alves",35)
Estudiante1 = Estudiante("Pedro","Lopez",40,"San Javier")

print(Persona1.getDatosPersonales())
print(Estudiante1.getDatosPersonales())
print("---------------------------------------")

Trabajador1 = Trabajador("Juan","Lopez",90,"McDonals")
Director1 = Director("Facundo","Tuñon",29,"Claro","San Patricio",40.5)

print(Trabajador1.getDatosPersonales())
print(Director1.getDatosPersonales())