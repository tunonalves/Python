class Persona():

	def Hablar(self):
		return "Hablo como una Persona"
	

class Trabajador(Persona):

	def Hablar(self):
		return "Hablo como un Trabajador"

class Director(Trabajador):

	def Hablar(self):
		return "Hablo como un Director"


def hablando(listadelaspersonas):
	for Persona in listadelaspersonas: #Persona hace polimorfismo
		print(Persona.Hablar())

antonio=Persona()
maria=Trabajador()
ana=Director()

print(antonio.Hablar())
print(maria.Hablar())
print(ana.Hablar())

print("----------------------------")


listaPersonas = [antonio,ana,maria]
hablando(listaPersonas)