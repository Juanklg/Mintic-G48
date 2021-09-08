import pandas as pd

rutaCsv = r'C:\Users\MakeDream\Desktop\Ruta1\Mintic-G48\Database\csv\\'
rutaXls = r'C:\Users\MakeDream\Desktop\Ruta1\Mintic-G48\Database\xls\\'

print("CSV".center(60,'-'))
data = {
    'first_name': ['Sigrid', 'Joe', 'Theodoric','Kennedy', 'Beatrix', 'Olimpia', 'Grange', 'Sallee'],
    'last_name': ['Mannock', 'Hinners', 'Rivers', 'Donnell', 'Parlett', 'Guenther', 'Douce', 'Johnstone'],
    'age': [27, 31, 36, 53, 48, 36, 40, 34],
    'amount_1': [7.17, 1.90, 1.11, 1.41, 6.69, 4.62, 1.01, 4.88],
    'amount_2': [8.06,  "?", 5.90,  "?",  "?", 7.48, 4.37,  "?"]
}

print("Dataframe desde Dict".center(60,'-'))
df = pd.DataFrame(data)
print(df)

print("csv desde DataFrame".center(60,'-'))
df.to_csv(rutaCsv+'example.csv')

print("leer csv desde ruta".center(60,'-'))
df = pd.read_csv(rutaCsv+'example.csv',
                        skiprows=1,
                        header=None,
                        names=['UID', 'First Name', 'Last Name', 'Age', 'Sales #1', 'Sales #2'],
                        index_col='UID',
                        na_values='?'
                        )
print(df)

print("Crear Excel desde DataFrame".center(60,'-'))
df.to_excel(rutaXls+'example.xlsx',sheet_name='example')

print("Modificando desde exel y guardando como CSV".center(60,'-'))
print("Leyendo csv modificado desde exel".center(60,'-'))
df = pd.read_csv(rutaCsv+'modificado.csv',
                    sep=';',
                    skiprows=1,
                    header=None,
                    names=['UID', 'First Name', 'Last Name', 'Age', 'Sales #1', 'Sales #2','Sales #3','E1','E2','E3'],
                    index_col='UID'
                    )
dfFinal = df.drop(['E1','E2','E3'], axis=1)
dfFinal = dfFinal.drop(df.iloc[8])
print(dfFinal)

print("Leyendo xls generado con DataFrame".center(60,'-'))
dfEx = pd.read_excel(rutaXls+'example.xlsx',sheet_name='example',index_col='UID')
print(dfEx)






