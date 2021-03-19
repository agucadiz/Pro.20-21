from lector import Lector
from libro import Libro
from datetime import datetime, timedelta

class Prestamo():

    __prestamos = {}

    @staticmethod
    def libros_prestados():
        return Prestamo.__prestamos

    def __init__(self, lector, libro, fecha_prestamo):
        if libro.codigo() in Prestamo.__prestamos:
            raise KeyError("El libro esta alquilado.")
        self.__lector = lector
        self.__libro = libro
        self.__fecha_prestamo = fecha_prestamo
        self.__fecha_devolucion = None
        Prestamo.__prestamos[self.__libro.codigo()] = self.__libro.titulo()
        self.__libro.set_prestado(True)

    def lector (self):
        return self.__lector

    def libro (self):
        return self.__libro

    def fecha_prestamos (self):
        return self.__fecha_prestamo

    def fecha_devolucion(self):
        return self.__fecha_devolucion

    def set_fecha_devolucion (self, fecha):
        self.__fecha_devolucion = fecha

    def devolver_libro(self, fecha):
        self.set_fecha_devolucion(fecha)
        #dias_prestamo = abs(self.fecha_devolucion() - self.fecha_prestamos()).days
        #if dias_prestamo > 15:
        #if self.__fecha_prestamo + timedelta(15) < self.__fecha_devolucion:
        self.lector().set_moroso(True)
        self.__libro.set_prestado(False)
        del Prestamo.__prestamos[self.__libro.codigo()]
