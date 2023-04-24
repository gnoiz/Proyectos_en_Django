#En lo posible, en VIEWS tenemos la parte lógica
#Y el código HTML se queda en la plantilla (MiPlantilla)


from django.http import HttpResponse
import datetime #con esto importamos un modulo para verificar el dia y hora
from django.template import Template, Context
from django.template import loader
from django.template.loader import get_template
from django.shortcuts import render

class Persona(object):
    def __init__(self, nombre, apellido):
        self.nombre =  nombre
        self.apellido = apellido


def saludo(request):    #primera vista
    
    p1 = Persona ("Cosme", "Fulanito")
    #nombre = "Cosme"
    #apellido = "Fulanito"
    temas_del_curso = ["Plantillas", "Modelos", "Formularios", "Vistas", "Despliegue"]
    lista_vacia_prueba = [ ]
    
    ahora = datetime.datetime.now()
    #001_  |FORMA NO ÓPTIMA| A través de esta manera cargamos las plantillas de HTML de forma manual, creamos una variable y utilizamos el metodo OPEN seguido de la ubicación del archivo entre parentesís
    #doc_externo = open("D:/006_Proyectos Django/MiPrimerProyecto/MiPrimerProyecto/Plantillas/MiPlantilla.html")   
    #005_   (Continuación de settings), creamos una variable para cargar los docs externos, especificando el nombre de la plantilla
    #doc_externo = loader.get_template('MiPlantilla.html')
    #comentamos la linea debido a que cambiamos las formas, from django.shortcuts import render/https://docs.djangoproject.com/en/4.1/topics/http/shortcuts    
    
    #002_   Creamos otra variable con el objeto TEMPLATE y le pasamos por parámetro el objeto que creamos anteriormente y con el metodo READ() le indicamos que lo lea:
    #plantilla = Template(doc_externo.read())   
    #Despues de leer abrir el mensaje y leerlo lo cerramos:
    #doc_externo.close()
    
    #contexto = Context({"nombre_persona":p1.nombre, "apellido_persona": p1.apellido, "fecha_hora_Actuales": ahora, "temas": temas_del_curso, "lvacia": lista_vacia_prueba })    #Diccionario, le pasamos 3 atributos + Lista []
    #contexto = Context({"nombre_persona":p1.nombre, "apellido_persona": p1.apellido, "fecha_hora_Actuales": ahora })    #Diccionario, le pasamos 3 atributos
    #contexto = Context({"nombre_persona": nombre, "apellido_persona": apellido, "fecha_hora_Actuales": ahora })       -Otra manera pero hay que crear las variables nombre y apellido previamente.
    #contexto = Context({"nombre_persona":Cosme, "apellido_persona": Fulanito})     -Es otra forma pero sin declarar variables previamente.
    #004_   |FORMA ÓPTIMA DE CARGAR TEMPLATES, SIGUE EN EL ARCHIVO "SETTINGS"|
    #003_   Soliciamos que renderice un objeto utilizando un contexto:
    #documento = plantilla.render(contexto)    
    
    #006_   Renderizamos el documento
    #documento = doc_externo.render({"nombre_persona":p1.nombre, "apellido_persona": p1.apellido, "fecha_hora_Actuales": ahora, "temas": temas_del_curso, "lvacia": lista_vacia_prueba })
    #comentamos la linea debido a que cambiamos las formas, from django.shortcuts import render/https://docs.djangoproject.com/en/4.1/topics/http/shortcuts/
    
    #return HttpResponse(documento)
    return render(request,"MiPlantilla.html",{"nombre_persona":p1.nombre, "apellido_persona": p1.apellido, "fecha_hora_Actuales": ahora, "temas": temas_del_curso, "lvacia": lista_vacia_prueba })

def saludo_Tere(request):    #primera vista
    return HttpResponse("<html><body><h1><i> Hola, Tere! <3 <i></h1></body></html>")


def despedida(request):
    return HttpResponse("Hasta luego xD")


def EjemploA(request):
    fecha_actual = datetime.datetime.now()
    return render(request,"EjemploA.html", {"fecha_hora_Actuales": fecha_actual})


def EjemploB(request):
    fecha_actual = datetime.datetime.now()
    return render(request,"EjemploB.html", {"fecha_hora_Actuales": fecha_actual})


def dame_el_dia(request):
    fecha_actual = datetime.datetime.now()
    
    documento = """
    <body>
    <h2>
    Fecha y hora actuales: %s
    </h2>
    </body>
    </html>""" % fecha_actual

    return HttpResponse(documento)

def calcula_edad(request, edad, agno):
    #edadActual = 34     
    periodo = agno - 2023
    edadFutura = edad + periodo
    agnoedadfutura= "<html><body><h2> En el año %s tendrás %s años</h2></body></html>" %(agno, edadFutura)
    return HttpResponse(agnoedadfutura)