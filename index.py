#primera impresion debe ser el saludo con el login

# variables = {int,float,str,bool,range,list,dict,tuple}
# funcines = {python,propias}
# sentecias de control = {if,while,for}

def isLogin(user)->bool:
    login = None
    if user=="Login":
        login = True
        print("Usuario logueado")
    else:
        login = False
        print("Usuario no logueado, stop")
        exit()

def detailVar(var:any):
    print("El valor es :",var)
    print("Es de tipo :",type(var))
    print("Su longitud es :",len(var))

user = "Login"
# user = "login"
isLogin(user)
# --------------------------------------------------------------------------------
print("Corriendo la app")


#tranformando a tupla
nombres3 = tuple(nombres3)
print(nombres3)

print(nombres3.count('Xavi'))
print(nombres3.index('Xavi'))
#En tuplas no existe el clear
# nombres3.clear()
# print(nombres3)

nombres4 = ('Otro',) + nombres3
print(nombres4)

recorrePalabras(nombres4)

#comparaciones de tuplas
t1 = (0,1,2) < (0,3,4)
print(t1)
#comparacion entre tuplas???
t1 = (1,1,20000) < (0,3,40000)
print(t1)

#La comparacion entre tuplas pérmite compara el pirmer elemento de cada tupla y solo incluir el segundo o el tercero en acso de empates
nombre = "Juan Linares"
t = nombre.split(' ')
(x,y)= t
print((x,y))
print((y,x))



#trasnformando a lista de nuevo
nombres3 = list(nombres3)
print(nombres3)

# Ver lista de funciones disponible spara la variable
# print(dir(nombres3))
# # limpiar la lista
nombres.clear()
print(nombres)
# # borrar la lista por completo
del nombres
# print(nombres)