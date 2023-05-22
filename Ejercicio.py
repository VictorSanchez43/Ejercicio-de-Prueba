import os
from collections import deque
from funcion_turnos import turnos()


my_deque = deque([])
os.system('cls')

while True:
    a = input('1- Registrar Turno.\n2- Salir del Sistema.\n\
        Ingrese una opcion: ')
    if a == '1':
        print('Por favor ingrese los datos del Paciente')
        nombre = input('Nombre y Apellido: ')
        dni = int(input('Dni: '))
        turnos(nombre, dni)
    elif a == '2':
        break
    else:
        input('Opcion incorrecta. Ingrese nuevamente los datos.')
        