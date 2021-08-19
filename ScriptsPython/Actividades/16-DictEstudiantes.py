def propiedadesIguales(pr):
    print(pr)
    if Estudiantes['Alumno1'][pr] == Estudiantes['Alumno2'][pr]:
        print('La propiedad es igual')
    else:
        print('La propiedad es diferente')

Estudiantes = {
    'Alumno1':{'nombre':'Daniel','edad':17,'estatura':1.56,'grupo':48},
    'Alumno2':{'nombre':'David','edad':17,'estatura':1.56,'grupo':48}
}

llaves = Estudiantes['Alumno1'].keys()
print(llaves)

for llave in llaves:
    propiedadesIguales(llave)




