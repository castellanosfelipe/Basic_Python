"""Una tupla es lo mismo que una lista solo que no se pueden modificar elementos
"""

numeros = (1, 2, 3, 4, 5) + (6, 7, 8)
print(numeros)
# crear tupla
punto = tuple([1, 2])
print(punto)
menosnumeros = numeros[:2]
print(menosnumeros)

primero, segundo, *otros = numeros
print(primero, segundo, otros)
