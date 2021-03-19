class Principal:
    from articulo import Articulo
    from cliente import Cliente
    from factura import Factura

    cliente1 = Cliente("48892365F", "Rosa", "González")
    televisor = Articulo(1, "TV Sonic", 399)
    tarjeta_g = Articulo(2, "Tarjeta graf. Sonic", 239)
    factura1 = Factura(cliente1)

    factura1.ayadir_linea(tarjeta_g, 1)
    factura1.ayadir_linea(televisor, 2)
    factura1.ayadir_linea(tarjeta_g, 1)

    factura1.lineas()
    factura1.eliminar_linea(1)
    factura1.lineas()

    factura1.imprimir_factura()
