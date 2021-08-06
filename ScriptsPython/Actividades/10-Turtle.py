from turtle import *

def crearFigura(lados,long):
    color('red','#11CD2F')
    begin_fill()
    for x in range(0,lados):
        fd(long)
        lt(360/lados)
    end_fill()

def crearTrazo(lim):
    fd(lim)
    bk(lim*2)

def crearCoor(lim):
    crearTrazo(lim)
    home()
    lt(90)
    crearTrazo(lim)
    home()

crearCoor(280)
done()