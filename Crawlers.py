import requests
from bs4 import BeautifulSoup

midoc = requests.get("http://python.beispiel.programmierenlernen.io/index.php")

docFinal = BeautifulSoup(midoc.text, "html.parser")

for cuerpoText in docFinal.select(".card-text"):
	print(cuerpoText.text)
	print("")
