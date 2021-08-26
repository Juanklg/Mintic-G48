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

def detailArch(el):
    print('---------------------------------')
    print(el)
    print("len = ",len(el))
    for i,e in zip(range(len(el)),el):
        print(f"Pos : {i} - Elemento : {e}")

#Funcion para imprimir un menu de numero y accion en consola
#recibe una tupla o una lista
def printMenu(el):
    print('---------------------------------')    
    for i,e in zip(range(1,len(el)+1),el):
        print(f"\t{i} - {e}")

