# esto carga el modulpo de turtle y me trae todas las librerias
from turtle import *

def crearFigura(lados:int,long:int):
    color('red','#11CD2F')
    begin_fill()
    for x in range(0,lados):
        fd(long)
        lt(360/lados)
    end_fill()

# def crearTrazo(lim):
#     fd(lim)
#     bk(lim*2)

# def crearCoor(lim):
#     crearTrazo(lim)
#     home()
#     lt(90)
#     crearTrazo(lim)
#     home()

# crearCoor(280)

def avanzar(a:int):
    """
    IN:valor actual del avance
    OUT:el valor de avance de rotob + el avance que llevava el robot
    """
    # a=a+10
    a+=10
    #estafuncion esde turtle fd(x) dodne x es igual a los pixele q avanza la tortuga
    fd(10)
    return a

def giro(g:int,side:str="D"):
    """
    IN:dos parametros
        g -> ingreso de los giros actuales del robot
        side-> sentido de giro "D" para derecha y "I"para izquierda
    
    por defecto el giro siempre es a la derecha

    """
    g+=1
    #segun el ingreso delside giramos a la derecha o a la izquierda segun el resultado del if
    if side == "D": 
        rt(90)
    elif side == "I":
        lt(90)
    #y al final retornamos el nuevo valor de g (giros)
    return g

#100 pixeles
def robotSquare():
    avance = 0
    giros = 0
    while giros < 4:
        avance = avanzar(avance)
        if avance == 100:
            avance=0
            giros = giro(giros)
    else: print("El robot termino el cuadrado")

# crearFigura(4,100)
# up()

robotSquare()

done()