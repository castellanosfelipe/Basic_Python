numeros = [
    2,
    4,
    5,
    65,
    45,
    654
]
# Ordenar en forma ascendente
numeros.sort(reverse=True)
# Ordena de forma descendente
numeros2 = sorted(numeros)


print(numeros)
print(numeros2)

usuarios = [
    [4, "chanchito"],
    [1, "felipe"],
    [2, "juan"]
]


# def ordena(elemento):
#     return elemento[1]


usuarios.sort(key=lambda el: el[1], reverse=True)
print(usuarios)
