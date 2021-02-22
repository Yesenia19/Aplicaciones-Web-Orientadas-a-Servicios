import web
import json
datos={}

urls = (
    '/edad?', 'Edad',
)

app = web.application(urls, globals())

class Edad:
  
  def datos(self,parametros):
    try:
      nombre = parametros.nombre
      fecha = parametros.fecha
  
      año=fecha[6:10]
      edad=2021-int(año)

      datos["Nombre"]=nombre
      datos["Fecha nacimiento"]=fecha
      datos["Edad"]=edad

      archivo = open("datos.txt","a")
      valores=("Nombre: " +nombre+ ", Fecha de nacimiento: " +fecha+ ", Edad: "+str(edad)+ "\n")
      archivo.write(valores)
      archivo.close()
      return json.dumps(datos)

    except:
      return "Los datos no fueron ingresados correctamente"

  
  def GET(self): 
    parametros = web.input() # Parametros por URL
    return self.datos(parametros) 	

  if __name__ == "__main__":
    app.run()