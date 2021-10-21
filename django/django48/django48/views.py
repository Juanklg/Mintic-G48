from django.http import HttpResponse
from django.template import loader
import datetime

def saludar(request):
    fechaActual = datetime.datetime.now()
    plt = loader.get_template('index.html')
    docu = plt.render({'fecha':fechaActual})
    return HttpResponse(docu)
    
def fonts(request):
    plt = loader.get_template('learncss/fonts.html')
    docu = plt.render()
    return HttpResponse(docu)

def tareas(request):
    taskList = ['Implementar db sqlite3','integrar vistas de flask']
    plt = loader.get_template('learndjango/tareas.html')
    docu = plt.render({"listado":taskList})
    return HttpResponse(docu)

def calculo(request,fechaNacimiento,fechaFutura):
    aActual = datetime.datetime.now().year
    edadActual = aActual - fechaNacimiento
    edadFutura = fechaFutura - fechaNacimiento
    dataCalculo={
        "agnoActual":aActual,
        "agnoNacimiento":fechaNacimiento,
        "agnoFUturo":fechaFutura,
        "edad":edadActual,
        "edadFutura":edadFutura,
    }
    plt = loader.get_template('learndjango/calculos.html')
    docu = plt.render(dataCalculo)
    return HttpResponse(docu)

# from django.template import Template, Context,loader

# doc_externo = open(r'C:\Users\MakeDream\Desktop\Ruta1\Mintic-G48\django\django48\django48\templates\layout.html')
# plt = Template(doc_externo.read())
# doc_externo.close()
# ctx = Context({

# doc_externo = open(r'C:\Users\MakeDream\Desktop\Ruta1\Mintic-G48\django\django48\django48\templates\layout.html')
# plt = Template(doc_externo.read())
# doc_externo.close()
# ctx = Context()
# docu = plt.render(ctx)
# return HttpResponse(docu)

# doc_externo = open(r'C:\Users\MakeDream\Desktop\Ruta1\Mintic-G48\django\django48\django48\templates\tareas.html')
# plt = Template(doc_externo.read())
# doc_externo.close()
# ctx = Context({"listado":taskList})
# docu = plt.render(ctx)
