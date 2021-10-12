from django.http import HttpResponse
from django.template import Template, Context
import datetime

def calculo(request,fechaNacimiento,fechaFutura):
    aActual = datetime.datetime.now().year
    # edadActual = aActual - fechaNacimiento
    # edadFutura = fechaFutura - fechaNacimiento
    documento = '''
        <!DOCTYPE html>
        <html lang="en">

        <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Calculo</title>
        </head>

        <body>
            <h1>Nacio en el año %s y tiene %s años</h1>
            <h1>En el %s este personaje tendra %s</h1>
        </body>

        </html>
    ''' % (fechaNacimiento,aActual-fechaNacimiento,fechaFutura,fechaFutura-fechaNacimiento)
    return HttpResponse(documento)

def fecha(request):
    fechaActual = datetime.datetime.now()
    documento = '''
        <!DOCTYPE html>
        <html lang="en">

        <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>
        </head>

        <body>
            <h1>El momento de la peticion fue %s</h1>
        </body>

        </html>
    ''' % fechaActual
    return HttpResponse(documento)

def saludar(request):
    doc_externo = open(r'C:\Users\MakeDream\Desktop\Ruta1\Mintic-G48\django\django48\django48\templates\layout.html')
    plt = Template(doc_externo.read())
    doc_externo.close()
    ctx = Context()
    docu = plt.render(ctx)
    return HttpResponse(docu)