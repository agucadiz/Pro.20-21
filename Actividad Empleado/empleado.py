class Empleado():

    def __init__(self, nombre, apellidos):
        self.__nombre = nombre
        self.__apellidos = apellidos

    def nombre(self):
        return self.__nombre

    def apellidos(self):
        return self.__apellidos

    def nombre_completo(self):
        return self.nombre() + " " + self.apellidos()

    def email(self):
        __email = self.nombre() + "." + self.apellidos() + "@company.com"
        return __email.lower()
