import web
import json
urls = (
    '/agenda?', 'Agenda',)    
app = web.application(urls, globals())

class Agenda():
  archivo_json = {}
  def GET(self):
    parametros = web.input()
    action = parametros.action 
   
    if action=="get":
      return self.getAction()

    if action=="put":
      try:
        nombre = parametros.nombre
        fecha = parametros.fecha
        año=fecha[6:10]
        edad=2021-int(año)
        
        persona = {
        "nombre": nombre,
        "edad": edad
        }
        with open("datos.json") as file:
          self.archivo_json = json.load(file) 
        self.archivo_json["agenda"].append(persona)
        print(self.archivo_json)  
        with open("datos.json","w") as file:
          json.dump(self.archivo_json, file)
        return(persona)
        
      except:
        return "Los datos no fueron ingresados correctamente"

  def getAction(self):
    try:
      with open("datos.json") as file:
        self.datos_json = json.load(file)
      return json.dumps(self.datos_json)     
    except Exception as error:
      print("Error {}".format(error.args[0]))

    	
  if __name__ == "__main__":
    app.run()
