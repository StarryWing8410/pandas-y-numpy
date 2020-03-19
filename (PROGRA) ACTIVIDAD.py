import pandas as pd
import time

listaEmpleado = {1:['Hector',1]}
empleado = pd.DataFrame(listaEmpleado)
empleado.index = ['Nombre', 'Departamento']

listaDepartamento = {1:['Desarrollo']}
departamento = pd.DataFrame(listaDepartamento)
departamento.index = ['Nombre departamento']
departamento

while True:
    try:
        empleado = pd.read_csv('empleado.csv', index_col = 0)
        print(f'{empleado.T}')
    except FileNotFoundError:
        print('*No se encontro el archivo\nRegistra empleados nuevos')
    print()
    try:
        departamento = pd.read_csv('departamento.csv', index_col = 0)
        print(f'{departamento.T}')
    except FileNotFoundError:
        print('*No se encontro el archivo\nRegistra departamentos nuevos')
        time.sleep(2)
    print('*' * 40)
    opcion = int(input('Selecciona una opcion:\n 1)Ingresar empleado                         2)Ingresar departamento\n 3)Mostrar registros                          4) Salir\n'))
    print('*' * 40)
    if opcion == 1:
        while True:
            claveEmpleado = len(empleado.columns) + 1
            print(f'*La clave del nuevo empleado es {claveEmpleado}')
            nombreEmpleado = str(input('*Ingresa el nombre del empleado: '))
            print(f'*El nombre del empleado es {nombreEmpleado}')
            print(departamento.T)
            claveDepartamentoEmpleado = int(input('*Ingrese la clave del departamento: '))
            print(f'*Se ha registrado al empleado {nombreEmpleado} con clave {claveEmpleado} en el departamento con clave {claveDepartamentoEmpleado}')
            empleado[claveEmpleado] = [nombreEmpleado, claveDepartamentoEmpleado]
            empleado.to_csv(r'empleado.csv', index = True, header  = True)
            print('*Registro guardado')
            decisionEmpleado = int(input('Agregar otro empleado\n1) Si         2) No\n'))
            print()
            if decisionEmpleado == 1:
                pass
            else:
                break
    elif opcion == 2:
        while True:
            claveDepartamento = len(departamento.columns) + 1
            print(f'*La clave del departamento es {claveDepartamento}')
            nombreDepartamento = str(input('*Ingresa el nombre del nuevo departamento: '))
            print(f'*El nombre del departamento es {nombreDepartamento}')
            print(f'*El departamento con clave {claveDepartamento} tiene por nombre {nombreDepartamento}')
            departamento[claveDepartamento] = [nombreDepartamento]
            departamento.to_csv(r'departamento.csv', index = True, header = True)
            print('*Registro guardado')
            decisionDepartamento = int(input('Agregar otro departamento\n1) Si         2) No\n'))
            if decisionDepartamento == 1:
                pass
            else:
                break
    elif opcion == 3:
        print(empleado.T)
        print()
        print(departamento.T)
        print()
        time.sleep(5)
    elif opcion == 4:
        print('Adios')
        break