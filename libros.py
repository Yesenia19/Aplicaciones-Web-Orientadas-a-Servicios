import requests
import json

libros = requests.get("https://www.googleapis.com/books/v1/volumes?q=harry+potter&callback=handleResponse")

book = libros.json()

libro_item = book["items"]

codificado = json.dumps(libro_item)
descifrado = json.loads(codificado)

print(descifrado[0]["volumeInfo"])
