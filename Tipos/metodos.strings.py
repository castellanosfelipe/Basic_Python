"""Texto para corregir error
"""

ANIMAL = "   chanchito feliz    "
# Toma el objeto que se encuentra y lo transforma todo a mayusculas
print(ANIMAL.upper())

# Toma el objeto que se encuentra y lo transforma todo a minusculas
print(ANIMAL.lower())

# Toma el primer caracter del objeto y lo transforma todo a mayuscula dejando el resto de la linea en minuscula
print(ANIMAL.capitalize())

# Toma el primer caracter de cada palabra y lo transforma a mayuscula dejando el resto en minuscula
print(ANIMAL.title())

# Remueve todos los espacios que esten a las izquierda y derecha de la oración
print(ANIMAL.strip())  # lstrip (izquierda), rstrip (derecha)

# Buscar la cadena e caracteres, si no la encuentra sale -1
print(ANIMAL.find("ch"))

# Reemplazar caracteres
print(ANIMAL.replace("cha", "j"))

# Confirmar si se encuentra o no (Boolean)
print("cha" in ANIMAL)

# Encadenar metodos
print(ANIMAL.strip().capitalize())
