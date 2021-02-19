import requests
import json

libros = requests.get("http://sesat.fdi.ucm.es:8080/servicios/rest/sinonimos/json/andar")

book = libros.json()
print(libros.headers["Content-Type"])
print("-----------------------------")
print(book.keys())
print("-----------------------------")
libro_item = book["sinonimos"]
print(libro_item)
print("-----------------------------")
codificado = json.dumps(libro_item)
descifrado = json.loads(codificado)

print(descifrado["sinonimo"])

