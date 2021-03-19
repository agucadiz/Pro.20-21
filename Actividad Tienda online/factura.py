class Factura:
    from articulo import Articulo

    __numero_fac = 0

    def __init__(self, cliente):
        Factura.__numero_fac += 1
        self.numero = Factura.__numero_fac
        self.__cliente = cliente
        self.__lineas = []

    def cliente(self):
        return self.__cliente

    def ayadir_linea(self, articulo, cantidad):
        self.__lineas.append([articulo, cantidad])

    def __precio_total(self):
        self.__precio_total = 0
        for i in self.__lineas:
            self.__precio_total += i[0].precio() * i[1]
        return self.__precio_total

    def eliminar_linea(self, numero):
        self.numero = numero
        if self.numero >= 1:
            self.numero -= 1
            del self.__lineas[self.numero]
        else:
            raise ValueError('El número introducido no es correcto.')

    def imprimir_factura(self):
        print(f'Nº FACTURA: {self.__numero_fac}')
        print(f'CLIENTE: {self.__cliente.nombre()} {self.__cliente.apellidos()}')
        print("ARTICULOS:")
        for i in self.__lineas:
            print(f'{i[1]} {i[0].denominacion()}')
        print("TOTAL:")
        print(self.__precio_total())

    def lineas(self):
        N = 1
        print("-" * 20)
        for i in self.__lineas:
            print(f'Linea {N} = {i[1]}, {i[0].denominacion()}')
            N += 1
        print("-" * 20)
