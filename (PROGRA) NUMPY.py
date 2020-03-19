import numpy as np

arreglo  = np.array([[10,20]])

print(arreglo)

while True:
    variable = int(input('Si quieres que siga escribe "1" si quieres que me detenga escribe "2": '))
    
    if variable == 2:
        break
    elif variable == 1:
        numero1 = int(input('Da un numero: '))
        numero2 = int(input('Da otro numero: '))
        arreglo = np.append(arreglo,[[numero1,numero2]], axis = 0)
    else:
        print('*Proporciona una opcion aceptable')
    
    print(f'*Los numeros en la lista son\n {arreglo}')
    