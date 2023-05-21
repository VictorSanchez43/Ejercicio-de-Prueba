import os
from collections import deque

my_deque = deque([])
os.system('cls')

while True:
    a = input('1- Registrar Turno.\n2- Salir del Sistema.\n\
        Ingrese una opcion: ')
    if a == '1':
        print('Por favor ingrese los datos del Paciente')
        nombre = input('Nombre y Apellido: ')
        dni = int(input('Dni: '))
        my_deque.append({'Nombre':nombre, 'DNI':dni})
        if len(my_deque) >= 3:
            print(f'Llamar al paciente:{my_deque.popleft()}')
            input('Presiona Enter para continuar')
            os.system('cls')
    elif a == '2':
        break
    else:
        input('Opcion incorrecta. Ingrese nuevamente los datos.')
        