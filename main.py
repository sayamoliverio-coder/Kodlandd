from flask import Flask
import random


app = Flask(__name__)

facts_list = [
    "Las nutrias marinas se toman de las manos al dormir para no separarse mientras flotan a la deriva en el agua.",
    "Los pulpos tienen tres corazones, nueve cerebros (uno central y uno en cada tentáculo) y sangre de color azul debido a que usan cobre en lugar de hierro para transportar oxígeno.",
    "El primer bug informático fue un insecto real: en 1947, los ingenieros de la computadora Harvard Mark II encontraron una polilla atrapada en un relé que provocaba un fallo en el sistema.",
    "La miel nunca se echa a perder: se han encontrado vasijas con miel de más de 3.000 años en tumbas egipcias que siguen siendo perfectamente comestibles.",
    "En Venus, un día dura más que un año: tarda más tiempo en dar una vuelta completa sobre su propio eje (243 días terrestres) que en dar la vuelta alrededor del Sol (225 días terrestres).",
    "Los wombats son los únicos animales conocidos que hacen caca en forma de cubo, lo que evita que ruede y les ayuda a marcar su territorio.",
    "La Universidad de Oxford es más antigua que el Imperio Azteca: se empezó a enseñar allí alrededor del año 1096, mientras que la fundación de Tenochtitlán ocurrió en 1325.",
    "Los plátanos son técnicamente bayas, pero las frutillas (fresas) no lo son desde el punto de vista botánico.",
    "El sonido del rugido de los leones en la película El Rey León (1994) en realidad se grabó utilizando tigres, ya que el rugido real de un león no sonaba lo suficientemente imponente en los micrófonos.",
    "En Suiza es ilegal tener una sola cobaya (cuy) como mascota, porque son animales extremadamente sociales y pueden sufrir depresión si viven solos.",
    "Tu nariz y tus orejas nunca dejan de crecer a lo largo de toda tu vida, debido a que están compuestas principalmente por cartílago que sigue cediendo ante la gravedad con los años."
    "El espacio exterior huele a metal caliente y carne quemada, según describen los astronautas cuando regresan de caminatas espaciales y se quitan sus trajes."
    "Los flamencos no nacen rosas: nacen con plumas grises y adquieren ese color por su dieta rica en camarones y algas que contienen carotenoides."
    "El inventor de las papas Pringles, Fredric Baur, estaba tan orgulloso de su diseño que pidió que parte de sus cenizas fueran enterradas dentro de uno de esos tubos cuando falleció en 2008."
    "Los tiburones existen desde antes que los árboles: los registros fósiles de tiburones datan de hace unos 400 millones de años, mientras que los primeros árboles aparecieron hace unos 350 millones."
    "El corazón de una ballena azul es tan grande que un ser humano pequeño podría nadar a través de sus arterias principales."
    "Las vacas tienen mejores amigas y muestran niveles medibles de estrés cuando son separadas de ellas."
    "La Torre Eiffel puede crecer hasta 15 centímetros en verano debido a la expansión térmica del hierro cuando hace mucho calor."
    "Los gatos no pueden percibir el sabor dulce porque carecen del receptor genético necesario en sus papilas gustativas."
    "Hay más estrellas en el universo observable que granos de arena en todas las playas y desiertos de la Tierra juntos."

]

@app.route("/")
def index():
    return '<h1>hola! Aquí podrás ver diferentes datos curiosos ❤️</h1><a href="/random_facts">¡Ver un hecho al azar!</a>'

@app.route("/random_facts")

def random_facts():
    return f"<p>{random.choice(facts_list)}</P>"

app.run(debug=True)