from modulos import isLogin
# -----------------------------------------------------------------------------------------------
def getProyectoByUser(p):
    return 'Proyecto retornado'

# -----------------------------------------------------------------------------------------------
print('Funciones'.center(50,'-'))
estudiantes_state = ('Activo','Invitado','Desconectado','Inactivo','Desactivado')
estuiantes_grupo = ('29','48','61')
estudiantes = {
    'proyectos':[{},{}],
    'user':'',
    'correo':'',
    'nombre':'',
    'grupo':'',
    'state':'',
}
listas_default = [
    {'nombre':'Roles','palabras':[],'color':'#0000ff'},
    {'nombre':'Acciones','palabras':[],'color':'#00ff00'},
    {'nombre':'Objetos','palabras':[],'color':'#ff0000'},
    {'nombre':'Nuevas','palabras':[],'color':'#ffffff'},
    {'nombre':'Descarte','palabras':[],'color':'#000000'},
]
lista = {
    'nombre':'',
    'palabras':[],
    'color':''
},
proyecto = {
    'Texto':'',
    'Palabras':[{}],
    'Listas':[{}],
    'Version':0.1
}
palabras_state = ('nuevas','clasificadas')
palabras = {
    'lista':'',
    'color':'',
    'palabra':'',
    'state':'Nuevas',
}

def returnUser(username):
    usuario = {
        'nombre':username,
        'edad':31,
        'admin':True,
        'count':15,
        "curso":"Curso de python",
        'correo':'juanlinares.ruta1@utp.edu.co',        
        "skills":{
            "Programacion":True,
            "BaseDeDatos":False
        },
        "numMedallas":10,
    }
    return usuario

