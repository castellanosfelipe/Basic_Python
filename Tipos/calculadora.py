""" Ajuste de error inicial
"""

N1 = input("Ingresa primer numero  ")
N2 = input("Ingresa segundo numero  ")

N1 = int(N1)
N2 = int(N2)

SUMA = N1 + N2
RESTA = N1 - N2
MULTIPLICACIÓN = N1 * N2
DIVISIÓN = N1 / N2

MENSAJE = f""""
Para los numero {N1} y {N2}
el resultado de la suma es {SUMA}.
el resultado de la resta es {RESTA}.
el resultado de la multiplicación es {MULTIPLICACIÓN}.
el resultado de la división es {DIVISIÓN}.
"""
print(MENSAJE)
