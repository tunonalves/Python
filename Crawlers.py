import requests

mireque = requests.get("https://www.latecla.info/actualidad")

print(mireque.status_code)
print(mireque.headers)
print(mireque.text)