import queue

sistema_solar = "Mercurio Venus Tierra Marte Jupiter Saturno Urano Neptuno Pluton"

planetas = set()

for planet in sistema_solar.split(" "):
	planetas.add(planet)

print(planetas)
print(len(planetas))

#micola = queue.Queue()
#micola = queue.LifoQueue()
micola = queue.PriorityQueue()

micola.put((3,"Argentina"))
micola.put((4,"Uruguay"))
micola.put((2,"Chile"))
micola.put((1,"Brasil"))

#print(micola.get())

for elemento in micola.queue:
	print(elemento)

