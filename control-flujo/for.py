"""Ajuste de error
"""
buscar = 10

for numero in range(5):
    print(numero, numero * 'hola mundo ')


for numero in range(5):
    print(numero)
    if numero == buscar:
        print('Encontrado ', buscar)
        break
else:
    print("No encontre el numero buscado")


for char in "Ultimate python":
    print(char)
