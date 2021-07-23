import requests
from bs4 import BeautifulSoup

mireque = requests.get("https://www.latecla.info/actualidad")
midoc = """
	<html>
		<body>
			<p> Este es el primer parrafo </p>
			
			<p> Este es el segundo parrafo </p>

			<a> es un vinculo </a>

		</body>
	</html>

"""

docFinal = BeautifulSoup(midoc, "html.parser")

for parrafo in docFinal.find_all("p"):
	print(parrafo.text)

#print(mireque.status_code)
#print(mireque.headers)
#print(mireque.text)

print(docFinal)