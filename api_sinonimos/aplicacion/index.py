import web
import requests
import json

render = web.template.render("aplicacion/")


class Index():
    def GET(self):
        sinonimos = None
        return render.index(sinonimos)

    def POST(self):
        form=web.input()
        palabra=form.palabra
        result = requests.get(
            'http://sesat.fdi.ucm.es:8080/servicios/rest/sinonimos/json/' +
            palabra)
        sinonimos = result.json()
        items = sinonimos["sinonimos"]
        encoded = json.dumps(items)
        decoded = json.loads(encoded)

        resultados = []

        for sinonimos in decoded:
            datos = {str(sinonimos)}
            resultados.append(datos)   

        return render.index(resultados)