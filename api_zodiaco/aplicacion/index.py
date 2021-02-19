import web
import json

render = web.template.render("aplicacion/")


class Index():
    def GET(sef):
      zodiaco = None
      return render.index(zodiaco)

    def POST(self):
        form = web.input()
        dia = int(form["dia"])
        meses = str(form["mes"])
        mes=meses.lower()

        aries = {} #21 de marzo - 20 de abril​
        aries["signo"]="Aries"
        aries["elemento"]="Fuego"
        aries["simbolo"]="Carnero"
        aries["numero_suerte"]="7, 17 y 21"
        aries["color"]=" Rojo, salmón y blanco"
        aries["domicilio"]="Marte"
        aries["horoscopo"]="Este año tendrás que plantearte buscar nuevos amigos porque es imposible seguir tu vida tan fiestera. Hacia la primavera, Plutón se posicionará en tu signo y hará que tus cejas se pueblen más de lo normal, por lo que deberás depilarte constantemente si no quieres que se queden las marcas del sol. Con la entrada del otoño, todo volverá a la normalidad y tu impulsividad favorecerá los golpes en la cabeza tan propios de ti."

        tauro = {} #21 abril -20 mayo
        tauro["signo"]="Tauro"
        tauro["elemento"]="Tierra"
        tauro["simbolo"]="Toro"
        tauro["numero_suerte"]="4, 6 y 11"
        tauro["color"]="Verde claro, rosa y turquesa"
        tauro["domicilio"]="Venus"
        tauro["horoscopo"]="Mientras que tus amistades y familiares conseguirán aumentos salariales, tu en cambio tendrás dificultades en el trabajo debido a conflictos con la secretaria de tu jefe. Además, tu adicción a las sabritas te llevará al borde de la ruina y pondrá en peligro la seguridad económica que tanto te preocupa. A pesar de todo, este año el amor te sonríe: si vas a Francia con frecuencia ten claro que el destino te pondrá a tiro al amor de tu vida, pero procura no comer sabritas si no, te vas a enfermar del estomago."

        geminis = {} #21 mayo – 20 junio
        geminis["signo"]="Geminis"
        geminis["elemento"]="Aire"
        geminis["simbolo"]="Gemelos"
        geminis["numero_suerte"]="3, 12 y 18"
        geminis["color"]="Azul, violeta y amarillo"
        geminis["domicilio"]="Mercurio"
        geminis["horoscopo"]="En 2030 aprovecharas cualquier fiesta de disfraces que se te presente para dar rienda suelta a tu bipolaridad, por lo mientas solo soñaras con ella.  Ganarás un concurso en Facebook y unos cuantos premios en el casino. ¡Este es tu año!, porfin seras millonario"
        
        cancer = {} #21 Junio – 21 Julio
        cancer["signo"]="Cancer"
        cancer["elemento"]="Agua"
        cancer["simbolo"]="Cangrejo"
        cancer["numero_suerte"]="2, 8 y 12"
        cancer["color"]="Blanco, plateado y verde"
        cancer["domicilio"]="Luna"
        cancer["horoscopo"]="Ese esfuerzo por ayudar a todo el mundo hará que te olvides de tu propia higiene: el jabón y el desodorante no formarán parte de tu vida. En cuanto al amor, si tienes pareja, esta te dejará por no ducharte. Y si no tienes pareja, obviamente seguirás sin tenerla. De momento, compra una escoba para limpiar tu cuarto desordenado."

        leo = {} #22 julio – 22 agosto
        leo["signo"]="Leo"
        leo["elemento"]="Fuego"
        leo["simbolo"]="León"
        leo["numero_suerte"]="1, 9 y 10"
        leo["color"]="Dorado, naranja y verde"
        leo["domicilio"]="Sol"
        leo["horoscopo"]="Durante los ultimos meses del año brillarás con luz propia, pero ten cuidado con las envidias, porque las venenosas de tus vecinas no descansaran hasta apagarla. Gozarás de buena salud casi todo el año, pero hacia los meses de otoño deberás prestar atención a posibles lesiones en los gluteos: tanto reggaeton te hara daño."

        virgo = {} #23 agosto – 22 septiembre
        virgo["signo"]="Virgo"
        virgo["elemento"]="Tierra"
        virgo["simbolo"]="Virgen"
        virgo["numero_suerte"]="10, 15 y 27"
        virgo["color"]="Blanco, violeta y naranja"
        virgo["domicilio"]="Mercurio"
        virgo["horoscopo"]="Gracias a tu esfuerzo y constancia, este año desarrollarás tu musculatura de una forma muy grande. Tendrás que ahorrar para comprarte ropa nueva; aprovecha y comprate algo sexy ahora que estás en forma. Eso sí, te recomendamos hacerte una limpieza dental profunda si no quieres espantar a la gente al sonreir."

        libra = {} #23 septiembre – 22 octubre
        libra["signo"]="Libra"
        libra["elemento"]="Aire"
        libra["simbolo"]="Balanza"
        libra["numero_suerte"]="2, 8 y 19"
        libra["color"]="Rosa, azul y verde"
        libra["domicilio"]="Venus"
        libra["horoscopo"]="Aunque eras muy feo al nacer, los años te han ido concediendo esa perfecta belleza que te define. Correrás el riesgo de que tu pareja se quede dormida al hacer el amor."

        escorpio = {} #23 Octubre – 21 Noviembre
        escorpio["signo"]="Escorpio"
        escorpio["elemento"]="Agua"
        escorpio["simbolo"]="Escorpión"
        escorpio["numero_suerte"]="4, 13 y 21"
        escorpio["color"]="Rojo, verde y negro"
        escorpio["domicilio"]="Plutón y Marte"
        escorpio["horoscopo"]="Piensa antes de actuar porque tu obsesión por ser la pareja de tu crush hara que se te vaya el amor de tu vida. Tus compañeros de trabajo pegarán chicles en tu silla para hacerte bajar de las nubes. Esté año no conseguirás caer bien a nadie, y tendrás suerte si consigues que alguien se ría de tus chistes malos."

        sagitario = {} #22 noviembre – 21 diciembre
        sagitario["signo"]="Sagitario"
        sagitario["elemento"]="Fuego"
        sagitario["simbolo"]="Centauro"
        sagitario["numero_suerte"]="9, 14 y 23"
        sagitario["color"]="Blanco, azul y verde"
        sagitario["domicilio"]="Júpiter"
        sagitario["horoscopo"]="Los astros te acompañan este año y tendrás un año de lo más divertido. Cuidado con el alcohol porque podrias ir al hospital. Podrás calmar tus ansias de alcohol si te apuntas a clases de salsa o de bachata, donde podrás dar rienda suelta a tu sensualidad de una forma más sutil."

        capricornio = {} #22 diciembre – 21 enero
        capricornio["signo"]="Capricornio"
        capricornio["elemento"]="Tierra"
        capricornio["simbolo"]="Cabra"
        capricornio["numero_suerte"]="3, 16 y 25"
        capricornio["color"]="Negro, azul y marrón"
        capricornio["domicilio"]="Saturno"
        capricornio["horoscopo"]="Dado tu materialismo y ambición, tendrías mucho éxito como banquero, pero este año te presentarás especialmente generoso. Serás muy comprensivo con los vagabundos y hasta se te pasará por la cabeza alojarlos en tu casa."

        acuario = {} #22 enero – 18 febrero
        acuario["signo"]="Acuario"
        acuario["elemento"]="Aire"
        acuario["simbolo"]="El Aguador"
        acuario["numero_suerte"]="7, 14 y 20"
        acuario["color"]="Gris, azul y verde"
        acuario["domicilio"]="Urano"
        acuario["horoscopo"]="Un dolor del corazón anidará en lo más íntimo de tu ser y te acompañará durante unos meses. La luna estará muy cerca de Tauro, lo que favorece los nuevos proyectos profesionales y la entrada de dinero en tu hogar. No decaigas, si eres capaz de controlar el estrés laboral, el corazón roto curara con el tiempo"

        piscis = {} #19 febrero – 20 marzo
        piscis["signo"]="Piscis"
        piscis["elemento"]="Agua"
        piscis["simbolo"]="Pez"
        piscis["numero_suerte"]="14, 25, 31, 39 y 58"
        piscis["color"]="Verde, azul y morado"
        piscis["domicilio"]="Neptuno y Júpiter"
        piscis["horoscopo"]="La alineación de los astros potenciará tu iniciativa en el amor, lo cual te vendrá muy bien para abandonar las  prácticas de cocina. Juguetes, disfraces y cremas de todo tipo habitarán tu mesita de noche. Pero no te confíes porque Marte entrará en tu signo hacia otoño, y tendrás problemas con los vecinos, que lo saben todo y son muy envidiosos."

        if (mes == "marzo" and dia >= 21) or (mes  == "abril" and dia  <= 20):
          result = json.dumps(aries)
          return render.index(result) 

        elif (mes == "abril" and dia >= 21) or (mes  == "mayo" and dia  <= 20):
          result = json.dumps(tauro)
          return render.index(result) 

        elif (mes == "mayo" and dia >= 21) or (mes  == "junio" and dia  <= 20):
          result = json.dumps(geminis)
          return render.index(result) 

        elif (mes == "junio" and dia >= 21) or (mes  == "julio" and dia  <= 21):
          result = json.dumps(cancer)
          return render.index(result)

        elif (mes == "julio" and dia >= 22) or (mes  == "agosto" and dia  <= 22):
          result = json.dumps(leo)
          return render.index(result) 
         
        elif (mes == "agosto" and dia >= 23) or (mes  == "septiembre" and dia  <= 22):
          result = json.dumps(virgo)
          return render.index(result) 

        elif (mes == "septiembre" and dia >= 23) or (mes  == "octubre" and dia  <= 22):
          result = json.dumps(libra)
          return render.index(result)   

        elif (mes == "octubre" and dia >= 23) or (mes  == "noviembre" and dia  <= 21):
          result = json.dumps(escorpio)
          return render.index(result) 

        elif (mes == "noviembre" and dia >= 22) or (mes  == "diciembre" and dia  <= 21):
          result = json.dumps(sagitario)
          return render.index(result) 
        
        elif (mes == "diciembre" and dia >= 22) or (mes  == "enero" and dia  <= 21):
          result = json.dumps(capricornio)
          return render.index(result) 

        elif (mes == "enero" and dia >= 22) or (mes  == "febrero" and dia  <= 18):
          result = json.dumps(acuario)
          return render.index(result)  
        
        elif (mes == "febrero" and dia >= 19) or (mes  == "marzo" and dia  <= 20):
          result = json.dumps(piscis)
          return render.index(result)

        else:
          datos="Los datos ingresados son incorrectos"
          result = json.dumps(datos)
          return render.index(result)