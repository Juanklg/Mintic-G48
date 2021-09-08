print("Txt".center(60,'-'))

rutaTxt = r'C:\Users\MakeDream\Desktop\Ruta1\Mintic-G48\Database\txt\\'
filename = 'lineas'

data = ['linea 1','linea 2','linea 3','linea 4','linea 5']
print("Crear archivo y escribir lineas".center(60,'-'))
file = open(rutaTxt+filename,'w')
for line in data:
    file.write(line)
    file.write('\n')
file.close()
print("Abrir archivo y agregar lineas".center(60,'-'))
file = open(rutaTxt+filename,'a')
for line in data:
    print('con a '+line,file=file)
file.close()

print("Abrir archivo y agregar lineas 2".center(60,'-'))
file = open(rutaTxt+filename,'a')
file.writelines('%s\n' % s for s in data)
file.close()

print("Abrir archivo y leer toda las lineas".center(60,'-'))
file = open(rutaTxt+filename,'r')
lines1 = file.readlines()
file.close()
lines1c = [s.rstrip('\n') for s in lines1]
print(lines1c)

print("Abrir archivo y leer linea por linea".center(60,'-'))
file = open(rutaTxt+filename,'r')
lines2=[]
for line in file:
    lines2.append(line)
file.close()
lines2c = [s.rstrip('\n') for s in lines2]
print(lines2c)
