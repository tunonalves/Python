sistema_solar = "Mercurio Venus Tierra Marte Jupiter Saturno Urano Neptuno Pluton"

planetas = set()

for planet in sistema_solar.split(" "):
	planetas.add(planet)

print(planetas)
print(len(planetas))
