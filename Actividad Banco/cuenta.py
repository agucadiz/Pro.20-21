class Cuenta:
    from cliente import Cliente
    from movimiento import Movimiento

    __numero_cuenta = 0
    __cuentas = {}

    def __init__(self, titular, saldo):
        Cuenta.__numero_cuenta += 1
        self.__titular = titular
        self.__saldo = saldo
        self.__numero = Cuenta.__numero_cuenta
        self.__movimientos = []
        Cuenta.__cuentas[self.__numero] = self

    def __repr__(self):
        return f'({self.__titular}, {self.__saldo})'

    def titular(self):
        return self.__titular

    def saldo(self):
        return self.__saldo

    def numero(self):
        return self.__numero

    def movimientos(self):
        return self.__movimientos

    def __set_saldo(self, cantidad):
        self.__saldo += cantidad

    def set_ayadir_movimiento(self, movimiento):
        self.__movimientos.append(movimiento)
        self.__set_saldo(movimiento.cantidad())

    @staticmethod
    def cuenta(numero):
        return Cuenta.__cuentas[numero]
