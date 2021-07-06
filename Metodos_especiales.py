import datetime

hoy=datetime.date.today();

print(str(hoy))
print(repr(hoy))
print("\n")


class Persona():

	datos_array=[]

	def __init__(self, *datos): #Es tupla en el constructor si se pone dos ** se transforma en diccionario
	    for dato in datos:
		    self.datos_array.append(dato)
	    self.getDatos(self.datos_array) #devuelve los datos


	def getDatos(self,info):
		for dato in info:
			print(dato)


	#def __str__(self): #pasa a string la info del objeto
	#	return "Datos: \n"+str(self.datos_array[0]) +"\n"+ str(self.datos_array[1]) + "\n" + str(self.datos_array[2])

	def __repr__(self): #pasa a string la info del objeto
		return "\n\nDatos: \n"+str(self.datos_array[0]) +"\n"+ str(self.datos_array[1]) + "\n" + str(self.datos_array[2])


p1 = Persona("Federico","Tuñon",34,"La Tecla")

print(p1)

class agenda():

	def __init__(self):
	    
	    self.miagenda={}
	
	def agregar_persona(self,nom,telefono):
		self.miagenda[nom]=telefono
	
	def __len__(self):
		return len(self.miagenda)
	

agendaPersonal= agenda()
agendaPersonal.agregar_persona("Fede","12312312312")
agendaPersonal.agregar_persona("juan","12312312311232")

print(len(agendaPersonal))
