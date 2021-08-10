from turtle import *

def crearFigura(lados:int,long:int):
    color('#5D11CD','#11CD2F')
    begin_fill()
    for x in range(0,lados):
        fd(long)
        lt(360/lados)
    end_fill()

def avazar(a):
    a += 10
    fd(10)
    return a

def giro(g:int,side:str="D"):
    g += 1
    if side=="D":
        rt(90)
    elif side=="I":
        lt(90)
    return g

def makeSquard(long:int,nGiros:int=4):
    avance = 0
    giros = 0
    while giros < nGiros:
        while avance < long:
            avance = avazar(avance)
        giros = giro(giros)
        avance = 0
    else:
        print("El dibujo esta completo")

def write(rgbTrace,rgbFill):
    color(rgbTrace,rgbFill)
    down()
    begin_fill()
    makeSquard(100)
    end_fill()
    up()

write("red","blue")









