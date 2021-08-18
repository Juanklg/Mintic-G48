#definimos unas variables con un valor inicial
x = 10
y = 10
#Variables type bool surgiendo de una comparacion
miBool = x == y
print(f"miBool es de tipo {type(miBool)}, y tiene un valor de : {miBool}")

# capturamos el texto que nos piden en el enunciado
varInputBool = input("Ingrese True/False para la segunda variable (True/False):")
print(f"El usuario ingreso en texto :{varInputBool}")

# convirtiendo una entrada de texto a tipo bool
if varInputBool=="True" or varInputBool=="False":
    varInputBool = True if varInputBool=="True"
else False

print(f"La variable 'varInputBool' convertida a booleano = {varInputBool}")

#Para trabajar con booleanos se utilizan las operaciones Logicas
# vamos a ver 3 tipos de operaciones logicas
#1-and, 2-or, 3-not

#3-not con el not invertimos el valor de una variable booleana
print(f"la variable miBool = {miBool} la invierto asi, 'not miBool'")
miBool = not miBool
print(f"la variable miBool ahora = {miBool}")if miBool: validador()
elif varInputBool: validador()
else condicionesFalsas() 


def condicionesFalsas():
    print(f"Ninguna de las dos variables es verdadera")

def validador():    
    if miBool == True and varInputBool == True:
        print(f"Las 2 variables son verdaderas")
    elif miBool == True or varInputBool == True:
        print(f"Alguna de las 2 es verdadera")
    else:
        print(f"Ninguna de las dos variables es verdadera")

if miBool: validador()
elif varInputBool: validador2()
else condicionesFalsas()
