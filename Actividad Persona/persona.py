class Persona:

    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad

    def __eq__(self, otro):
        if not isinstance(otro, type(self)):
            return NotImplemented
        return (self.__nombre, self.__edad) == (otro.__nombre, otro.__edad)

    def __hash__(self):
        return hash((self.__nombre, self.__edad))

    def __repr__(self):
        return f'Persona({self.__nombre}, {self.__edad})'

    def __str__(self):
        return f'Se trata de {self.nombre()}, con edad {self.edad()}.'

    def nombre(self):
        return self.__nombre

    def edad(self):
        return self.__edad

    def compara_edad(self, otro):
        if self.edad() > otro.edad():
            print(f'{otro.nombre()} es más joven que yo.')
        elif self.edad() < otro.edad():
            print(f'{otro.nombre()} es más viejo que yo.')
        else:
            print(f'{otro.nombre()} tiene la misma edad que yo.')
