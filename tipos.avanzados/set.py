""" set significa grupo o conjunto
"""

primer = {1, 1, 2, 2, 3, 4}
segundo = [3, 4, 5]
segundo = set(segundo)
# primer.add(5)
# primer.remove(1)
# el operador | hace una unión de los set que se le pasen
# print(primer | segundo)
# Arroja los elementos en comun de los set
# print(primer & segundo)
# Arroja solo los datos del conjunto de la izquierda que no esten en la derecha
# print(primer - segundo)
# Arroja los datos que no se encuentren entren iguales en los dos
print(primer ^ segundo)
