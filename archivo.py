# Esta funcion es para realizar los turnos
import os
from collections import deque
my_deque = deque([])

nombre = 'nombre'
dni = 'numero'


def turnos(nombre, dni):
    my_deque.append({'Nombre':nombre, 'DNI':dni})
    if len(my_deque) >= 3:
        print(f'Llamar al paciente:{my_deque.popleft()}')
        input('Presiona Enter para continuar')
        os.system('cls')