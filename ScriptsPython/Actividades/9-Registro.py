print("Para el registro se solictan los siguientes datos")
nombre = input("Ingrese nombre :")
edad = input("Ingrese edad (debe ser en numeros) : ")
altura = input("Ingrese altura (en numeros) : ")
rolAdmin = input("Ingrese rol Administrador True/False : ")

try:    
    edad = int(edad)
    altura = float(altura)
    #convirtiendo nuestro ingreso en la variable rolAdmin a Booleano    
    if rolAdmin=="True" or rolAdmin=="False":
        rolAdmin = True if rolAdmin=="True" else False
    else:exit()
    #como no se cumplio la condicionforzo el erro y lanza la except
    
#si no lanza ningun error continua el codigo normal
#si lanza algun error retorna el bloque de codigo despues del except
except:
    print("Alguno de los valores ingresados no es correcto")
    print("vuelva a correr la aplicacion")
    #le damos fin a la aplicacion por error del usuario
    exit()

print(f''' Registro Exitoso
    Nombre = {nombre}
    Edad = {edad}
    Altura = {altura} metros
    Administrador = {rolAdmin}
''')

# en caso del rol ser True usamos despues el operador not para trasnformarlo a false
if rolAdmin==True:
    print("El usuario no puede ser administrador entonces actualizamos su rol")
    rolAdmin = not rolAdmin
    print(f''' Registro actualizado
        Nombre = {nombre}
        Edad = {edad}
        Altura = {altura} metros
        Administrador = {rolAdmin}
    ''')
