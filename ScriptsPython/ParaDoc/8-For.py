from time import sleep

#Bucle tipo for
# arreglo = range(10,15)
# print(type(arreglo))
# print(len(arreglo))

# for valor in arreglo:    
#     print(valor)
# else:
#     print(f"Imprimio todos los valores")

# miRange = range(1,11)
# print(f"la logitud de miRange es {len(miRange)} valores")
# print(miRange)



# #for para recorrer objetos
# for valor in miRange:
#     print(valor)

def splitText(texto, patron):
    lista = texto.split(' ')
    return lista

def forConRangeIncremental():
    for j in range(0,10,2):
        sleep(.5)
        print("Estamos en la iteracion ",j)
        if(j==6): continue

def forParaStrings():
    texto = "Hola python desde fundamentos de programacion"
    for caracter in texto:
        print("este es el caracter",caracter)
        sleep(.5)        
        if(caracter != 'y'): continue
        else: 
            print("Cuando encuentre la 'y' imprima esto y salga")
            break

def forBasico():
    for x in range(0,3):
        print("La iteracion es igual ",x)

def recorrePalabras(palabras):
    for palabra in range(len(palabras)):
        print(palabra)
        print(palabras[palabra])
        print("Palabra: {0}, en la frase su posicion es : {1}".format(palabras[palabra], palabra))

def dbConnection(config):
    for p in config:
        print(p)
    return "psql -h {server} -p {port} -U {user} -d {dbname}".format(
        server=config[0],
        port=config[1],
        user=config[2],
        dbname=config[3],
    )

# forBasico()
# forParaStrings()
# forConRangeIncremental()

listaManual = [
    "Xavi",
    "Juan",
    "Wendy"
]

texto = "Hola python desde fundamentos de programacion"
listaDePalabras = splitText(texto,' ')
print("las palabras son",listaDePalabras)
print("La cantida de palabras es",len(listaDePalabras))
recorrePalabras(listaDePalabras)

print(listaDePalabras[len(listaDePalabras)-1])

# con = dbConnection(["237.0.0.1","5432","root","nomina"])
# print(con)

