#primera impresion debe ser el saludo con el login
# variables = {int,float,str,bool,range,list,dict,tuple}
# funcines = {python,propias}
# sentecias de control = {if,while,for}
from datetime import datetime
import crudXls as crud

def isLogin(user)->bool:
    login = None
    if user=="Login":
        login = True
        print("Usuario logueado")
    else:
        login = False
        print("Usuario no logueado, stop")
        exit()

def detailVar(var:any):
    print("El valor es :",var)
    print("Es de tipo :",type(var))
    print("Su longitud es :",len(var))

def detailArch(el):
    print('---------------------------------')
    print(el)
    print("len = ",len(el))
    for i,e in zip(range(len(el)),el):
        print(f"Pos : {i} - Elemento : {e}")

#Funcion para imprimir un menu de numero y accion en consola
#recibe una tupla o una lista
def printMenu(el):
    print('---------------------------------')    
    for i,e in zip(range(1,len(el)+1),el):
        print(f"\t{i} - {e}")

#Funciones de base de datos con excel

def menuFinal(rut):
    #lista de parametros para creacion
    task = ("Nombre","Descripcion","Estado","Inicio","Fin")
    #Lista de opciones para el menu de el cli
    opciones = ("Create","Read","Update","Delete","Exit")
    #Filtros para buscar en la base de datos
    filterState = ["Todas","Pendientes","Ejecucion","Revision","Finalizada"]
    #Sub menu de opciones de estado de las tareas q se agregan
    menuState = filterState[1:]

    while True:
        opcion=''
        print('---------------------------------')
        printMenu(opciones)
        opcion=input('Digite la opcion deseada: ')
        print("\nUsted selecciono la opcion",opcion)
        if not(opcion=="1") and not(opcion=="2") and not(opcion=="3") and not(opcion=="4") and not(opcion=="5"):
            print("Comando Invalido")
        elif opcion=="1":#Create
            dictTask=dict.fromkeys(task)        
            print('\n* Crear nueva Tarea *')

            print('\n* Nombre *') 
            dictTask['Nombre']=input('Indique el Nombre de la tarea : ')

            print('\n* Descripcion *') 
            dictTask['Descripcion']= input('Indique la descripcion de la tarea : ')

            dictTask['Estado']='Pendientes'
            now = datetime.now()
            dictTask['Inicio']=str(now.day) +'/'+ str(now.month) +'/'+str(now.year)
            dictTask['Finalizada']=''
            crud.Create(rut, dictTask)
        elif opcion=="2":#Read
            printMenu(filterState)
            opcion=input('\nIndique la lista de tareas que quiere revisar: ')
            print("\nUsted selecciono la opcion",opcion)
            if not(opcion=="1") and not(opcion=="2") and not(opcion=="3") and not(opcion=="4"):
                print("Comando Invalido")
            elif opcion=="1":
                print('* Consultando Todas Las tareas*') 
                crud.Read(rut, 'Todas')
            elif opcion=="2":
                print('* Consultando las tareas Pendientes*')
                crud.Read(rut, 'Pendientes')
            elif opcion=="3":
                print('* Consultando las tareas Ejecucion*')
                crud.Read(rut, 'Ejecucion')
            elif opcion=="4":
                print('* Consultando las tareas Revision*')
                crud.Read(rut, 'Revision')
            elif opcion=="5":
                print('* Consultando las tareas Finalizada*')
                crud.Read(rut, 'Finalizada')
        elif opcion=="3":#update
            dictTask=dict.fromkeys(task)
            print('\n* Actualizar Tarea *')
            id=int(input('Indique el Id de la tarea que desea actualizar: '))

            print('\n* Nuevo titulo *')
            print('*Nota: si no desea actualizar el titulo solo oprima ENTER')
            dictTask['Nombre']=input('Indique el nuevo titulo de la tarea : ')
            
            print('\n* Nuevo Descripcion *')
            print('*Nota: si no desea actualizar el titulo solo oprima ENTER')
            dictTask['Descripcion']=input('Indique la descripcion de la tarea : ')

            print('\n* Nuevo Estado *')
            printMenu(menuState)
            print('*Nota: si no desea actualizar el titulo solo oprima ENTER')        
            newState = int(input('Indique el nuevo estado de la  tarea : '))
            dictTask['Estado'] = filterState[newState]
            if newState == 4:
                now = datetime.now()
                dictTask['Fin'] = str(now.day) +'/'+ str(now.month) +'/'+str(now.year)
            crud.Update(rut,id,dictTask)
        elif opcion=="4":#delete        
            print('* ELiminar Tarea **') 
            id=int(input('Indique el Id de la tarea que desea eliminar: '))
            crud.Delete(rut, id)
        elif opcion=="5":exit()

def menuOriginal(rut):
    datosActualizados = {
        'titulo':'',
        'descripcion':'',
        'estado':'',
        'fechaInicio':'',
        'fechaFinalizacion':'',
    }

    while True:
        print('Indique la accion que desea realizar: ')
        print('\t 1-Consultar')
        print('\t 2-Actualizar')
        print('\t 3-Crear nueva tarea')
        print('\t 4-Borrar')
        accion = input('Escriba la opccion: ')

        if not(accion=="1") and not(accion=="2") and not(accion=="3") and not(accion=="4"):
            print('Comando invalido por favor eliga una opcion valida')
        elif accion=='1': 
            opc_consulta='' 
            print('Indique las tareas que desea consultar: ') 
            print('\t 1-Todas las tareas') 
            print('\t 2-En espera') 
            print('\t 3-En ejecucion') 
            print('\t 4-Por aprobar') 
            print('\t 5-Finalizada') 
            opc_consulta = input('Digite las tareas que desea consultar: ')
            print("Consulta",opc_consulta)
            if opc_consulta=='1': 
                print() 
                print() 
                print('* Consultando todas Las tareas *') 
                crud.leer(rut, 'todo') 
            elif opc_consulta=='2': 
                print() 
                print() 
                print('* Consultando tareas en espera *') 
                crud.leer(rut, 'En espera') 
            elif opc_consulta=='3': 
                print() 
                print() 
                print('* Consultando tareas en ejecucion *') 
                crud.leer(rut, 'En ejecucion') 
            elif opc_consulta=='4': 
                print() 
                print() 
                print('* Consultando tareas por aprobar *') 
                crud.leer(rut, 'Por aprobar') 
            elif opc_consulta=='5': 
                print() 
                print() 
                print('* Consultando tareas finalizadas *') 
                crud.leer(rut, 'Finalizada')
        elif accion=='2': 
            datosActualizados={'titulo':'', 'descripcion':'', 'estado':'', 'fecha inicio':'', 'fecha finalizacion':''}
            print('* Actualizar Tarea *') 
            print() 
            id_Actualizar=int(input('Indique el Id de la tarea que desea actualizar: ')) 
            print() 
            print('* Nuevo titulo *') 
            print('*Nota: si no desea actualizar el titulo solo oprima ENTER') 
            datosActualizados['titulo']=input('Indique el nuevo titulo de la tarea : ') 
            print() 
            print('* Nueva descripcion *') 
            print('Nota: si no desea actualizar la descripcion solo oprima ENTER') 
            datosActualizados[ 'descripcion']= input('Indique La nueva descripcion de la tarea : ') 
            print() 
            print('* Nueva estado **') 
            print('En espera: 2') 
            print('En ejecucion: 3') 
            print('Por aprobar 4') 
            print('Finalizada: 5')
            print('**Nota: si no desea actualizar el estado solo oprima ENTER') 
            estadoNuevo= input('Indique el nuevo estado de la tarea : ') 
            if estadoNuevo=='2': 
                datosActualizados['estado']='En espera' 
            elif estadoNuevo=='3': 
                datosActualizados[ 'estado']='En ejecucion' 
            elif estadoNuevo=='4': 
                datosActualizados[ 'estado']='Por aprobar' 
            elif estadoNuevo=='5': 
                now = datetime.now() 
                datosActualizados['estado']='Finalizada' 
                datosActualizados['fecha finalizacion']=str(now.day) +'/'+ str(now.month) +'/'+str(now.year) 
                
            now = datetime.now() 
            datosActualizados['fecha inicio']=str(now.day) +'/'+ str(now.month) +'/'+str(now.year) 
            crud.actualizar(rut,id_Actualizar, datosActualizados) 
            print()
        elif accion=='3': 
            datosActualizados={'tarea':'', 'descripcion':", 'estado':'", 'fecha inicio':'', 'fecha finalizacion':''} 
            print('* Crear nueva Tarea *') 
            print() 
            print('* titulo *') 
            print() 
            datosActualizados['titulo']=input('Indique el titulo de la tarea : ')
            print() 
            print('* descripcion *') 
            datosActualizados['descripcion']= input('Indique la descripcion de la tarea : ')
            print() 
            datosActualizados['estado']='En espera' 
            now = datetime.now() 
            datosActualizados['fecha inicio']=str(now.day) +'/'+ str(now.month) +'/'+str(now.year) 
            datosActualizados['fecha finalizacion']=''
            crud.agregar(rut, datosActualizados) 
        elif accion=='4': 
            print('') 
            print('* ELiminar Tarea **') 
            iden=int(input('Indique el Id de la tarea que desea eliminar: '))
            crud.borrar(rut, iden)

rut = r"C:\Users\MakeDream\Desktop\Ruta1\Mintic-G48\dbTask.xlsx"
print("Imprimiendo variable dunder name en funciones = ",__name__)
if __name__ == '__main__':
    menuFinal(rut)
