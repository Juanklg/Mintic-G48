print("Pandas".center(60,'-'))
import pandas as pd
import numpy as np

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
print(almacen.sample(7))
print(almacen.sample())

print("Metodo describe and info".center(60,'-'))
# Se puyede agregar include o exclude
print(almacen.describe())
print(almacen.info())

print("Metodo value_counts".center(60,'-'))
s = pd.Series([3, 1, 2, 1, 1, 4, 1, 2, np.nan])
print(s)
print(s.value_counts(dropna=False))#dropna false incluye los NaN
print("Metodo value_counts bins".center(60,'-'))
print(s.value_counts())
print(s.value_counts(bins = 4))

print("seleccion de datos en Series, rangos".center(60,'-'))
print(ven)
print("".center(60,'-'))
print(ven[1:])
print("".center(60,'-'))
print(ven[:1])
print("".center(60,'-'))
print(ven['Ene':'Feb'])
print("Series uso de rango iloc".center(60,'-'))
print(ven.iloc[1])
print(ven.iloc[-1])
print(ven.iloc[[-1,0]])
print(ven.iloc[0:2])

print("sub series por medio de arrays y bools".center(60,'-'))
s = pd.Series([5, 2, -3, 7, 8, 4])
print(s)
print(s[[True, False, False, True, True, False]])
print(s[s>2])
print("sub series por medio de arrays y bools (loc e iloc)".center(60,'-'))
print(s.loc[[True, False, False, True, True, True]])
print(s.loc[s>2])
# print(s.iloc[s>2]) #genera error
res = (s>2).values
print(res)
print(s.iloc[res])

print("Dataframes Seleccion indices y etiquetas".center(60,'-'))
df = pd.DataFrame(np.arange(18).reshape([6, 3]),
                 index = ["a", "b", "c", "d", "e", "f"],
                 columns = ["A", "B", "C"])

print(df)
print("get indice columnas".center(60,'-'))
getlocCL = df.columns.get_loc("B")
print(getlocCL)
getIndexerCL = df.columns.get_indexer(["A", "C"])
print(getIndexerCL)
print("get indice index(Rows)".center(60,'-'))
getLoc = df.index.get_loc("d")
getIndexer = df.index.get_indexer(["c", "e"])
print(getLoc)
print(getIndexer)

print("DataFrame extraer informcion de una etiqueta".center(60,'-'))
pos = df.index.get_loc("c")
co = df.iloc[pos, 2]
print(co)
co = df.iloc[[5, 3], df.columns.get_indexer(["C", "A"])]
print(co)

print("DataFrame uso de listas de booleanos".center(60,'-'))
df = pd.DataFrame(np.arange(18).reshape([6, 3]),
                 index = ["a", "b", "c", "d", "e", "f"],
                 columns = ["A", "B", "C"])

print(df)
# mask = [True, False, True,False, False,True]
mask = (df.A>7)
print(mask)
print(df[mask])
print("uso de listas de booleanos con loc".center(60,'-'))
print(df.loc[df.B>6])
print("uso de listas de booleanos con iloc".center(60,'-'))
print(df.iloc[(df.B>6).values])

print("DataFrame seleccion aleatoria ".center(60,'-'))
print(df)
dfSample = df.sample(3, random_state = 18)
print(dfSample)
dfSample = df.sample(2, random_state = 18, axis = 1)
print(dfSample)

print("Metodo DataFrame pop".center(60,'-'))
df = pd.DataFrame(np.arange(15).reshape([3, 5]), 
                  index = ["a", "b", "c"],
                  columns = ["A", "B", "C", "D", "E"])
print(df)
print(df.pop('B'))
print(df)

print("Series Metodo Series pop y drop".center(60,'-'))
s = pd.Series([1,2,3,4,5],index=["a", "b", "c","d", "e"])
print(s)
print(s.drop("b"))
print(s)
print(s.drop(["d","a"]))

print("Serie Metodo Where".center(60,'-'))
s = pd.Series(np.arange(0, 10))
print(s)
print(s.where(s%2==0,0.0))

print("Edicion DataFrame".center(60,'-'))
print(df)
df.iloc[1,2] = -1
print(df)
df['A'] = 10
print(df)
df['A'] = [10,20,30]
print(df)
print("Edicion DataFrame otro".center(60,'-'))
df = pd.DataFrame(np.arange(12).reshape([4, 3]),
                  index = ["a", "b", "c", "d"],
                  columns = ["A", "B", "C"])

print(df)
df.loc["b":"c", "A":"B"] = [[-1, -2], [-3, -4]]
print(df)
df.loc["b":"c", "A":"B"] = -1
print(df)

print("Edicion DataFrame where".center(60,'-'))
df = pd.DataFrame(np.arange(12).reshape(-1, 3), columns=["A", "B", "C"])
print(df)
print(df.where(df % 2 == 0,-df))

print("Edicion DataFrame drop".center(60,'-'))
df = pd.DataFrame(np.arange(16).reshape([4, 4]), 
                  index = ["a", "b", "c", "d"],
                  columns = ["A", "B", "C", "D"])

print(df.drop(["a", "c"], axis = 0))

print("Union de series".center(60,'-'))
s = pd.Series([1, 2, 3, 4, 5,], index = ["a", "b", "c", "d", "e"])
r = pd.Series([10, 11, 12], index = ["f", "g", "h"])

print(s)
print(r)
t = pd.concat([s, r])
print(type(t))
print(t)

print("Union de series con axis,sort".center(60,'-'))

a = pd.Series([1, 2, 3, 4, 5,], index = ["a", "b", "c", "d", "e"])
b = pd.Series([10, 11, 12], index = ["a", "b", "f"])
r = pd.concat([a, b], axis = 1, sort = True)
print(r)

s = pd.Series([1, 2, 3, 4], index = ["a", "b", "c", "d"])
r = pd.Series([10, 11, 12], index = ["a", "c", "e"])
print(pd.concat([s, r]))

print("Appende de series ".center(60,'-'))
a = pd.Series([1, 2, 3, 4, 5], index = ["a", "b", "c", "d", "e"])
b = pd.Series([10, 11, 12], index = ["f", "g", "h"])

print(a)
print(b)
print(a.append(b))