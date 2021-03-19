from empleado import Empleado

emp1 = Empleado('María', 'García', 60000)
emp2 = Empleado.desde_cadena('Juan-Pérez-55000')

print(emp1.nombre())
print(emp1.salario())
print(emp2.nombre())
print(emp2.salario())
