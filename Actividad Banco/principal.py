from cliente import Cliente
from movimiento import Movimiento
from cuenta import Cuenta

cliente1 = Cliente('48892364E', 'Antonio', 'Martínez')
cuenta1 = Cuenta(cliente1, 100)
cuenta2 = Cuenta(cliente1, 200)

cuenta1.set_ayadir_movimiento(Movimiento('Nómina', 1000))
cuenta1.set_ayadir_movimiento(Movimiento('Primark', -100))
cuenta1.set_ayadir_movimiento(Movimiento('Mercadona', -50))

cuenta2.set_ayadir_movimiento(Movimiento('Nómina', 1200))
cuenta2.set_ayadir_movimiento(Movimiento('GYM', -50))
cuenta2.set_ayadir_movimiento(Movimiento('Venta', 1000))

print(cuenta1.saldo())
print(cuenta2.saldo())

print(cuenta1.movimientos())
print(cuenta2.movimientos())

print(cuenta1.titular())
print(cuenta2.titular())

print(cuenta1.numero())
print(cuenta2.numero())

s = Cuenta.cuenta(1)
print(s)
