def detailArch(el):
    print('---------------------------------')
    print(el)
    print("len = ",len(el))
    for x in range(len(el)):
        print(f"Pos : {x} - Elemento : {el[x]}")
    # for x in el:
    #     print(f"Elemento : {x}")

#tranformando a tupla
nombres = ["Thomas","Xavi","Abraham","Juan"]

nombres2 = tuple(nombres)
print(nombres)

#concatenando tuplas en nueva tupla
nombres2 = ('Xavi',) + nombres2
print(nombres2)

print(nombres2.count('Xavi'))
primerpos = nombres2.index('Xavi')
print(primerpos)
print(nombres2.index('Xavi',primerpos+1))

detailArch(nombres2)


#comparaciones de tuplas
t1 = (0,1,2) < (0,3,4)
print(t1)
#comparacion entre tuplas???
t1 = (0,1,20000) < (0,3,40000)
print(t1)

#La comparacion entre tuplas pérmite compara el pirmer elemento de cada tupla y solo incluir el segundo o el tercero en acso de empates
#desembalaje, unpackage
nombre = "Juan Linares"
t = nombre.split(' ') #convertimos a un list o (Array) la t de len 2
(x,y)= t
print(x)
print(y)

#trasnformando a lista de nuevo
nombres3 = list(nombres2)
print(nombres3)

# Ver lista de funciones disponible spara la variable
# print(dir(nombres3))

#En tuplas no existe el clear
# nombres2.clear()
print(nombres2)

# # limpiar la lista
nombres3.clear()
print(nombres3)
# # borrar la lista por completo
del nombres3
# print(nombres)

#patron DSU
print(nombres)
#derorate
l=list()
for nombre in nombres:
    l.append((len(nombre),nombre))
#sort
l.sort(reverse=True)
#undecorate
res = list()
for longitud,nombre in l:
    res.append(nombre)

print(res)
