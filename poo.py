class Coche():
	ruedas = 4
	largoChasis = 260
	anchoChasis = 130
	arrancado = False
	def __init__(self,ruedas,largoChasis,anchoChasis):
		self.ruedas = ruedas
		self.largoChasis = largoChasis
		self.anchoChasis = anchoChasis

	def arrancar(self):
		self.arrancado = True
	def parar(self):
		self.arrancado = False

miCoche = Coche()

print(miCoche.ruedas)
miCoche.arrancar()
print(miCoche.arrancado)

