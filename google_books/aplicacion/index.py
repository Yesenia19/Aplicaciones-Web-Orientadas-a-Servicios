import web
import requests
import json

render_app = web.template.render("aplicacion/")

class Index():

    def GET(self):
        return render_app.index()

    def POST(self):
        form = web.input()
        libro_name = form.nombre_libro
        

        libros_all = requests.get("https://www.googleapis.com/books/v1/volumes?q="+libro_name)

        libro = libros_all.json()
        

        libro_item = libro["items"]

        codificado = json.dumps(libro_item)
        descifrado = json.loads(codificado)

        url = descifrado[0]["volumeInfo"]["infoLink"]
        url_imagen=descifrado[0]["volumeInfo"]["imageLinks"]["smallThumbnail"]
        nombre_autor=str(descifrado[0]["volumeInfo"]["authors"])

        link ="<a href='"+url+"'> Link de compra</a>"
        imagen ="<img src='"+url_imagen+"'/>"

        informacion = ("<p>" + imagen + "<p> Nombre: " + libro_name  + "<p> Autor: " + nombre_autor)
        return (link + informacion)

        

        
        