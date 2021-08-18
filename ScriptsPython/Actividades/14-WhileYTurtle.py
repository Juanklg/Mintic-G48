from turtle import *

pd()

def movimientos():
    # promedio, total, contar = 0.0, 0, 0
    print("Introduzca letra para el movimiento (e para salir)")
    letra = input()
    while letra != "e":
        if letra=="a": fd(10)
        elif letra=="b": bk(10)
        elif letra=="d": rt(90)
        elif letra=="i": lt(90)
        elif letra=="u": up()
        elif letra=="dw": pd()
        else: print("Esta letra no tiene un movimiento asignado")
        print("Introduzca letra para el movimiento (e para salir)")
        letra = input()
    else:
        print("Figura terminada")
        pu()
        home()
        done()

movimientos()