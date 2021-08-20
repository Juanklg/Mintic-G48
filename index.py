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

# diccionario = {
#     'IDE':'Integrated Development Environment',
#     'OOP':'Object Oriented Programming',
#     'DBMS':'Database Management System'
# }

# #largo
# print('Largo',len(diccionario))
# # acceder a un elemento (key)
# print( diccionario['IDE'])
# print(diccionario.get('IDE'))
# # modificando elementos
# diccionario['IDE'] = 'integrated development environment'
# print( diccionario['IDE'])
# # recorrer los elementos
# for termino, valor in diccionario.items():
#     print(termino, valor)

# for termino in diccionario.keys():
#     print(termino)

# for valor in diccionario.values():
#     print(valor)

# # comprobar existencia de algún elemento
# print('OOP' in diccionario)

# # agregar un elemento
# diccionario['PK'] = 'Primary Key'
# print(diccionario)

# # remover un elemento
# diccionario.pop('DBMS')
# print(diccionario)

# # limpiar
# diccionario.clear()
# print(diccionario)

# # eliminar el diccionario
# del diccionario
# # print(diccionario)

# Definir una lista de tipo str
nombres = ['Juan','Karla','Ricardo', 'María',15,5.9]
# imprimir la lista nombres
print(nombres)
# acceder a los elementos de un a lista
print(nombres[0])
print(nombres[1])
# acceder a los elementos de manera inversa
print(nombres[-1])
print(nombres[-2])
#Imprimir un rago
print(nombres[0:2]) # sin incluir el índice 2
#Ir del inicio de la lista al índice (sin incluirlo)
print(nombres[:3])
#Desde el índice indicado hasta el final
print(nombres[1:])
#Cambiar un valor
nombres[3] = 'Ivone'
print(nombres)
#iterar una lista
for nombre in nombres:
    print(nombre)
else:
    print('No existen más nombres en la lista')
# preguntar el largo de una lista
print(len(nombres))
# agregar un elemento
nombres.append('Lorenzo')
print(nombres)
# insertar un elemento en un índice en específico
nombres.insert(1, 'Octavio')
print(nombres)
# remover un elemento
nombres.remove('Octavio')
print(nombres)
# remover el último valor agregado
nombres.pop()
print(nombres)
# eliminar un indice
del nombres[0]
print(nombres)
# limpiar la lista
nombres.clear()
print(nombres)
# borrar la lista por completo
del nombres
print(nombres)
