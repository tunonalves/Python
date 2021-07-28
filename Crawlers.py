import requests
from bs4 import BeautifulSoup

midoc = requests.get("http://python.beispiel.programmierenlernen.io/index.php")

docFinal = BeautifulSoup(midoc.text, "html.parser")

iconos = docFinal.select(".emoji")

print(iconos[0].text)