#definimos nuestra funcion
def sumaSimple(n1:int,n2:int) -> int:
    res = n1 + n2
    return res

def funcionSinArgs() :
    print("Aca empieza la funcion")
    print("Aca termina la funcion")

def probandoPass(): pass

#sin parametros pero llama a otra funcion
def repetir_funciones():
    print("corriendo repetir funciones")
    imprime_cosas()
    imprime_cosas()
#sin parametros y sin retorno
def imprime_cosas():
    print("Cosa 1")
    print("Cosa 2")
#Funcion completa
def BeneficiosOPerdidas(ingresos:int,gastos:int=1000000):
    """
    Esta funcion me calcula si hay ganacias o perdidas
    Basado en los ingresos y los gastos totales
    Ingresos y los gastos deben ser e typo int
    """
    print(f"Ingresos = {ingresos}")
    print(f"Gastos = {gastos}")
    if ingresos > gastos:
        valorResultado = ingresos-gastos
        resultado = "Ganancia = "+str(valorResultado)
    elif ingresos == gastos:
        valorResultado = gastos-ingresos
        resultado = "Sin ganacias ni perdidas"
    else:
        valorResultado = gastos-ingresos
        resultado = "Perdida = "+str(valorResultado)
    return [resultado,valorResultado]

def dentroDelRango(v:int,vm=5,vM=35)->bool:
    '''
    Ingresa 3 valores
    El valor a validar dentro del rango
    El valor minimo del rango
    El valor maximo del rango
    '''
    dentroRango = v >= vm and v <= vM
    if dentroRango:
        print(f'El valor {v} está dentro de rango')
    else:
        print(f'El valor {v} está fuera de rango')
    return dentroRango


ingresos = 5000
gastos = 2000

#uso de las funciones definidas
funcionSinArgs()
resultadoSuma = sumaSimple(7, 5)
repetir_funciones()

#diferentes formas de llamar a la funcion y de asignar sus parametros
print(BeneficiosOPerdidas(3000))
print(BeneficiosOPerdidas(3000, 7000))
res = BeneficiosOPerdidas()
print(res[1])

print(f"el resultado es {dentroDelRango(5)}")
dentroDelRango(5,2,10)
dentroDelRango(5,6)
dentroDelRango(vM=20,v=18,vm=15)
dentroDelRango()