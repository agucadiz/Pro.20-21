from persona import Persona


p1 = Persona('Samuel', 24)
p2 = Persona('Jael', 36)
p3 = Persona('Liliana', 24)

p1.compara_edad(p2)
p2.compara_edad(p1)
p1.compara_edad(p3)

print(p1.__eq__(p1))
print(p1.__eq__(p2))

print(hash(p1))

print(Persona.__repr__(p1))

print(Persona.__str__(p2))

print(p1)
