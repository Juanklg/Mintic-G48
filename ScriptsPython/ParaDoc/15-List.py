def recorrePalabras(palabras):
    for palabra in range(len(palabras)):
        print(palabra)
        print(palabras[palabra])
        print("Palabra: {0}, en la frase su posicion es : {1}".format(palabras[palabra], palabra))


# # Definir una lista de tipo str
nombres = ['Juan','Karla','Ricardo', 'María',15,5.9]
# # imprimir la lista nombres
print(nombres)
# # acceder a los elementos de un a lista
print(nombres[0])
print(nombres[1])
# # acceder a los elementos de manera inversa
print(nombres[-1])
print(nombres[-2])
# #Imprimir un rago
print(nombres[0:2]) # sin incluir el índice 2
#Ir del inicio de la lista al índice (sin incluirlo)
print(nombres[:3])
# #Desde el índice indicado hasta el final
print(nombres[1:])
# #Cambiar un valor
nombres[3] = 'Ivone'
print(nombres)
# #iterar una lista
for nombre in nombres:
    print(nombre)
else:
    print('No existen más nombres en la lista')
# # preguntar el largo de una lista
print(len(nombres))
# # agregar un elemento
nombres.append('Lorenzo')
print(nombres)
# # insertar un elemento en un índice en específico
nombres.insert(1, 'Octavio')
print(nombres)
# # remover un elemento
nombres.remove('Octavio')
print(nombres)
# # remover el último valor agregado o elñ index q se suministre
nombres.pop(-2)
print(nombres)
# # eliminar un indice
del nombres[-2]
print("Lista final",nombres)

nombres2 = ["Xavi","Juan","Daniela"]
#extend
nombres.extend(nombres2)
print(nombres)
#conunt
print("Count",nombres.count('Juan'))
#Index
print("Index",nombres.index('Juan',0,6))
# copy
nombres3 = nombres.copy()
#reverse
nombres.reverse()
print(nombres)
#sort a-z
nombres.sort()
print(nombres)
#sort reverse z-a
nombres.sort(reverse=True)
print(nombres)
nombres3.remove('Juan')
print(nombres3)
#recorrer la union de dos listas al mismo tempo
for ordenada, extendida in zip(nombres,nombres3):
    print("Ordenada",ordenada,"Extendidad",extendida)