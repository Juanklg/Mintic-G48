print("Pandas".center(60,'-'))
import pandas as pd

print("Series".center(60,'-'))
ven = pd.Series([15,28,97],index=["Ene","Feb","Mar"])
print(ven)

print("Index Series".center(60,'-'))
print(ven[0])
print(ven['Mar'])

print("Actualizando un valor".center(60,'-'))
ven['Mar']=64
print(ven)

print("Leyendo valores e indices".center(60,'-'))
print(ven.index)
print(ven.values)

print("Atributo name".center(60,'-'))
ven.name = 'Ventas 2021'
ven.index.name = 'Meses'

print("Atributo axes y shape".center(60,'-'))
print(ven.shape)
print(ven.axes)

print("DataFrames desde dict".center(60,'-'))
datos = {"manzanas":[3,2,0,1],"naranjas":[0,3,7,2]}
compras = pd.DataFrame(datos,index=['Mateo','Kevin','Juan','Wendy'])
print(compras)

print("DataFrames indice".center(60,'-'))
print(compras.index)
print(compras.columns)

print("DataFrames axesand shape".center(60,'-'))
print(compras.axes)
print(compras.shape)

print("DataFrames atributo name".center(60,'-'))
compras.index.name = 'Clientes'
compras.columns.name = 'Frutas'
print(compras)

print("DataFrames values".center(60,'-'))
print(compras.values)

print("Serie con tuplas".center(60,'-'))
tup = pd.Series([15,28,97],index=[("Ene",59),("Feb",78),("Mar",31)])
print(tup)

# -----------------------------dataframes y series-------------------

print("Creacion de series dict 3 datos principales".center(60,'-'))
d = {'Mar':8,'Ene':6,'Feb':1}
s= pd.Series(d,index={"Mar","Feb","Ene","Abr"},dtype=int)
print(s)

print("Creacion de DataFrames (dict) $ datos principales".center(60,'-'))

elementos = {
    'Numero Atomico':[1,6,47,88],
    'Masa atomica':[1.008,12.485,107.34,124],
    'familia':['No metal','metal','metal','metal']
}
tp = pd.DataFrame(elementos)
print(tp)

print("DataFrames (dict) row for dict".center(60,'-'))
uni = [
    {"Ag":2, "Au":5, "Cu":3, "Pt":2},
    {"Ag":4, "Au":6, "Cu":7, "Pt":2},
    {"Ag":3, "Pb":2, "Cu":4, "Pt":1}
]
unidades = pd.DataFrame(uni,index=[2015,2016,2017])
print(unidades)


print("Metodos".center(60,'-'))

entrada = [11, 18, 12, 16, 9, 16, 22, 28, 31, 29, 30, 12]
salida = [9, 26, 18, 15, 6, 22, 19, 25, 34, 22, 21, 14]
meses = ["ene", "feb", "mar", "abr", "may", "jun", "jul", "ago","sep", "oct", "nov", "dic"]

print("Entradas".center(60,'-'))
entradas = pd.Series(entrada,index = meses)
print(entradas)

print("Salidas".center(60,'-'))
salidas = pd.Series(salida,index = meses)
print(salidas)

print("Almacen".center(60,'-'))
almacen = pd.DataFrame({'entradas':entradas,'salidas':salidas})
almacen["neto"] = almacen.entradas - almacen.salidas
print(almacen)

print("Metodo Head,tail, sample".center(60,'-'))
#captura los prinerois 5
print(almacen.head())
# Captura los ultimos 5 elemenots
print(almacen.tail())
# 
print(almacen.sample(2))
print(almacen.sample(2))
print(almacen.sample(2))

print("Metodo describe and info".center(60,'-'))
# Se puyede agregar include o exclude
print(almacen.describe())
print(almacen.info())

