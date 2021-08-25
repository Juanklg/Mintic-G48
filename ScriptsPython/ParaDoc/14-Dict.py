

#dict
miDict = {}
miDictFunct = dict(nombre='Juan',clase='Fundamentos de programacion')
#crear un dict
miDict = {
    ('IDE',78694):'Integrated Development Environment',
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

telefonos = {
    ('Juan','Linares'):'3145782312'
}

print(telefonos['Juan'])

diccionario = {
    'IDE':'Integrated Development Environment',
    'OOP':'Object Oriented Programming',
    'DBMS':'Database Management System'
}

# #largo
print('Largo',len(diccionario))
# # acceder a un elemento (key)
print( diccionario['IDE'])
print(diccionario.get('IDE'))
# # modificando elementos
diccionario['IDE'] = 'integrated development environment'
print( diccionario['IDE'])
# # recorrer los elementos y 0ordernarlos por clave
print(diccionario.items())
order = list(diccionario.items())
order.sort()
print(order)
#Revisar ordenar con llave compuesta 

for termino, valor in diccionario.items():
    print(termino, valor)

for termino in diccionario.keys():
    print(termino)

for valor in diccionario.values():
    print(valor)

# # comprobar existencia de algún elemento
print('OOP' in diccionario)

# # agregar un elemento
diccionario['PK'] = 'Primary Key'
print(diccionario)

# # remover un elemento
diccionario.pop('DBMS')
print(diccionario)

# # limpiar
diccionario.clear()
print(diccionario)

# # eliminar el diccionario
del diccionario
# print(diccionario)

