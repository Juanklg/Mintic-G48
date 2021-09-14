import pandas as pd
def casos(ruta_archivo: str)-> dict:
    listaRespuesta = []
    df = pd.read_csv(ruta_archivo,index_col='ID de caso')
    # print(df)
    # d = df.sample(20)
    # d1 = df.columns.get_loc()
    # d1 = df.columns.get_indexer([[:],'Departamento o Distrito'])
    a=df['Departamento o Distrito']
    b=df['Edad']
    r = pd.concat([a, b], axis = 1, sort = True)
    print(r)

    promedio_edad = r['Edad'].mean()#.round(4)
    print(promedio_edad)
    


    




    return listaRespuesta

print(casos(r'C:\Users\MakeDream\Desktop\Ruta1\Mintic-G48\Database\csv\casos.csv'))

# print("DataFrame extraer informcion de una etiqueta".center(60,'-'))
# pos = df.index.get_loc("c")
# co = df.iloc[pos, 2]
# print(co)
# co = df.iloc[[5, 3], df.columns.get_indexer(["C", "A"])]
# print(co)