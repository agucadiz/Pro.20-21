class Movimiento:
    def __init__(self, concepto, cantidad):
        self.__concepto = concepto
        self.__cantidad = cantidad

    def __repr__(self):
        return f'({self.__concepto}, {self.__cantidad})'

    def concepto(self):
        return self.__concepto

    def cantidad(self):
        return self.__cantidad
