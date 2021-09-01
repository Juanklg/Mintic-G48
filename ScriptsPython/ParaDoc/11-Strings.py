#practivas grupo 48

#variables numericas y input(los input's siempre seran de type 'str')
x = int(input("Ingrese x : "))
y = int(input("Ingrese y : "))
print(x)
print(type(x))


#variables de texto o str o string
ciudad = "Bogota"
comentario = "\"Me gusta Python\""
numero = 123456789

# Imprimiendo Strings concatenados
print("Juan es de "+ciudad+" y dice \n"+comentario+" y digito un numero"+str(numero))

# Imprimiento un texto con unas variables internas
print(f"Juan es de {ciudad} y dice \n{comentario} y digito un numero {numero}")
# pritn con comas no necesita trasnformacion de tipos
print("Juan es de",ciudad,"y dice\n",comentario)
# print tambien acepta textos entre comilla simple
print('Comentario con comilla simple',numero)

tercio = 1.0/3
print("Un tercio = %f"%tercio)
print("Un tercio = %.2f" %tercio)

var = "Juan dice : \n\"Me gusta python\""
#asi se hacen comentarios de multimples lineas

#este meotdo nos permite imprimir tanto int como str
print("El valor de x =",x)
print("El valor de y =",y)

#Este solo me permite imprimir str, sirve para concatenar str
print("El formador "+var)

print(f"El valor de x = {x}")
print(f"El valor de y = {y}")

print(f"variable numero es de tipo {type(numero)}")
print(f"variable var es de tipo {type(var)}")

resultado = x + y + numero
# resultado = x + y# + numero
print(f"El resultado es {resultado}")

#practicas grupo 29

x = int(input("Digite un valor para x : "))
y = int(input("Digite un valor para y : "))

print("x es de tipo = ",type(x))
print("y es de tipo = ",type(y))
"""
#para concatenas str
print("el valor de x = "+x+" y el valor de Y = "+y+" y su suma ="+x+y)
#para imprimir valores separados
print("el valor de x =",x,"y el valor de Y =",y,"y su suma =",x+y)
"""
#para imprimir textos con variables internas
print(f"el valor de x = {x} y el valor de Y = {y} y su \"suma\" = {x+y}")

# var = 20
# print(var)
# var = "Hola"
# print(var)

#asi se imprime en varias lineas
print(f''' Registro Exitoso
    Nombre = {nombre}
    Edad = {edad}
    Altura = {altura} metros
    Administrador = {rolAdmin}
''')

var = 31
    hexa = 0x31
    print("El en hexa = %d y el numero en decimal es = %d" % (hexa,var))