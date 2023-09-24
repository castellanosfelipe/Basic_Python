mascotas = [
    "Felipe",
    "pipe",
    "pulga",
    "pulga",
    "chanchito feliz"
]

mascotas.insert(1, "melvin")
# Elemento agregar al final de la lista
mascotas.append("chanchito triste")
# Eliminar solo el primer elemento asi este repetido
mascotas.remove("pulga")
# Eliminar solo el ultimo elemento de un arreglo
mascotas.pop()
# Eliminar elemento en posición 0
del mascotas[0]
# Eliminar el arreglo completo
mascotas.clear()
print(mascotas)
