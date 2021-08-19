def splitText(texto, patron):
    lista = texto.split(' ')
    return lista

def ordenAlfabetico(palabra,palabra2):
    if palabra < palabra2:
        print("Tu palabra, "+palabra+", viene antes de "+palabra2)
    elif palabra > palabra2:
        print("Su palabra, "+palabra+", viene despues de "+palabra2)
    else:
        print("Su palabra es "+palabra2)

texto = "Hola python desde fundamentos de programacion"
listaDePalabras = splitText(texto,' ')

# detailVar(listaDePalabras)
detailVar(texto)

#acediendo a una posicion especifica
# nv = listaDePalabras[3]

#los numeros no son iterables
# detailVar(str(1234567))
# nv = str(1234567)

#extrayendo una sub lista
nv = texto[:5]
#strip elimina los espacion al principo y al final
nv=nv.strip()

# Comparando str en orden alfabetico
if nv=="Hola":print("Correcto")
else : print("Incorrecto")

# Organizando los srt en orden alfabetico a modo de python
ordenAlfabetico("hola","Hola")

#capitalize
st = "hola"
print("Esto hace el capitalize",st.capitalize())

#casefold
st = texto
print("Esto hace el casefold",st.casefold())

#endswith
print("endswith con 'cion' es = ",st.endswith('cion'))

#startswith
print("startswith con 'Hola' es = ",st.startswith('Hola'))

#upper
# st = texto.upper()
# detailVar(st)

#lower
# st = texto.lower()
# detailVar(st)

#find
# index = st.find("F")
# print(index)

#Formatos con simbolo %
# camellos = 42
# st = r"He visto %X camellos" %camellos
# print(st)

#count
# st = texto
# primera = st.find('a')
# print(primera)
# print(st.count('a',primera+1))

#Replace
st = "un uno, un dos, un tres"
print(st.replace("un","xxx",2))

#format
st = "un {mese}, un {dias}, un {años}".format(mese=12,dias=7,años=89)
print(st)
st = "un {0}, un {1}, un {0}".format(12,7,89)
print(st)

#Concatenar y multiplicar
st = "texto uno"
st2 = "texto dos"
stf = st*2+" "+st2
print(stf*3)

#añadir
st = "Hola "
st+="Juan, "
st+="grupo 48 "
print(st)