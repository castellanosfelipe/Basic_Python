usuarios = [
    ["chanchito", 2],
    ["felipe", 4],
    ["juan", 6]
]


# nombres = []
# for usuario in usuarios:
#     nombres.append(usuario[0])
# print(nombres)
# Creamos nueva lista con expresiones resumidas para transformarlas(map)
# nombres = [usuario[0] for usuario in usuarios]

# Filtrar(filter) elementos sin transformarlos
# nombres = [usuario for usuario in usuarios if usuario[1] > 2]
# Filtrar(filter) y tranformar(map)
# nombres = [usuario[0] for usuario in usuarios if usuario[1] > 2]
# misma operación de transformar(map) pero con la declaración del metodo map
# nombres = list(map(lambda usuario: usuario[0], usuarios))
# misma operación de filtrado(filter) pero con la declaración del metodo filter
menosusuarios = list(filter(lambda usuario: usuario[1] > 2, usuarios))
print(menosusuarios)
