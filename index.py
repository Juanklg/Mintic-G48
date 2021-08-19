#primera impresion debe ser el saludo con el login

# variables = {int,float,str,bool,range,list,dict,tuple}
# funcines = {python,propias}
# sentecias de control = {if,while,for}

# Login
login = True
if login:
    print("Usuario logueado")
else:
    print("Usuario sin registro")

def detailVar(var:any):
    print("El valor es :",var)
    print("Es de tipo :",type(var))
    print("Su longitud es :",len(var))
# --------------------------------------------------------------------------------

#dict
miDict = {}
miDictFunct = dict(nombre='Juan',clase='Fundamentos de programacion')
#crear un dict
miDict = {
    'IDE':'Integrated Development Environment',
    'OPP':'Object Oriented Programming',
    'DBMS':'Database Management System',
    'API':'Application Programming Interface'
}

usuario = {
    'nombre':'Juan',
    'edad':31,
    'admin':True,
    'count':15,
    "curso":"Curso de python",
    'correo':'juanlinares.ruta1@utp.edu.co',
    'dict':miDict,
    "skills":{
        "Programacion":True,
        "BaseDeDatos":False
    },
    "numMedallas":10,
}

employees = {
    "employees":[
        {"firstName":"John", "lastName":"Doe"},
        {"firstName":"Anna", "lastName":"Smith"},
        {"firstName":"Peter", "lastName":"Jones"}
    ]
}
#actuaizando alguno de sus valores
# print(usuario['curso'])
usuario['curso']="Fundamentos de programacion"
# print(usuario['curso'])
# print(usuario['skills'])

#funcion dir para ver metodos de una variable
# detailVar(usuario)
# print(dir(usuario))

#clear
# print(employees)
employees.clear()
print(employees)

#copy
# employees = usuario.copy()
# print(employees)

#fromkeys
# students = dict.fromkeys(['Xavi','Abraham','Juan','daniela'])
students = dict.fromkeys(('Xavi','Abraham','Juan','daniela'))
print(students)

#get
nv = usuario.get('curso')
print(nv)
nv = usuario['curso']
print(nv)

#items -> me retorna una lista de tuplas con las llaves y los valores
nv = usuario.items()
# print(nv)

#keys
nv = usuario.keys()
# print(nv)

#pop -> elimina un elemnto del dicciopnario con su llave
usuario.pop('numMedallas')
# print(usuario)

#popitem
# usuario.popitem()

#setdefault
# usuario.setdefault()

#update
usuario.update(grupo='48')
usuario.update(count=usuario['count']+1)
# print(usuario)

#values
nv = usuario.values()
# print(nv)

#len
print(len(usuario))
print(usuario)

del usuario['skills']

print(usuario)