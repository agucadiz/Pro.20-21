class Empleado:

    def __init__(self, nombre, apellidos, salario):
        self.__nombre = nombre
        self.__apellidos = apellidos
        self.__salario = salario

    @staticmethod
    def desde_cadena(cadena):
        parametro = cadena.split("-")
        return Empleado(parametro[0], parametro[1], parametro[2])

    def nombre(self):
        return self.__nombre

    def apellidos(self):
        return self.__apellidos

    def salario(self):
        return self.__salario
