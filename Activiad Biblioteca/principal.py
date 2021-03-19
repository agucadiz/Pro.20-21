from lector import Lector
from libro import Libro
from prestamo import Prestamo
from datetime import datetime

lector1 = Lector(1, "Ana", "García")
lector2 = Lector(2, "Roberto", "Sánchez")
libro1 = Libro(0, "El camino", "Miguel Delibes", "Salvat")
libro2 = Libro(1, "Cien años de soledad", "Gabriel García Márquez", "Planeta")
libro3 = Libro(2, "Rayuela", "Julio Cortázar", "Planeta")

prestamo1 = Prestamo(lector1, libro1, datetime(2021, 2, 22))
prestamo2 = Prestamo(lector1, libro2, datetime(2021, 2, 23))
prestamo3 = Prestamo(lector2, libro3, datetime(2021, 2, 1))

"""
print(f'El lector número {lector2.numero()} es moroso: {lector1.moroso()}')
prestamo3.devolver_libro(datetime(2021, 2, 10))
print(f'El lector número {lector2.numero()} es moroso: {lector1.moroso()}')
"""

print(f'El lector {lector1.nombre()} {lector1.apellidos()} es moroso: {lector1.moroso()}')
prestamo1.devolver_libro(datetime(2022, 4, 22))
print(f'El lector {lector1.nombre()} {lector1.apellidos()} es moroso: {lector1.moroso()}')
