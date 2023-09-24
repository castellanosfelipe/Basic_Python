"""Ajustar error
"""
# Saber si el string es palindromo


def es_palindromoV2(texto):
    """
    Verifica si un string es un palíndromo.

    Parámetros:
    - string: El string que se desea verificar.

    Retorna:
    - True si el string es un palíndromo.
    - False si el string no es un palíndromo.
    """
    # Convertir el string a minusculas y eliminar espacios
    texto = texto.lower().replace(" ", "")

    # Verificar si el string es igual al string invertido
    if texto == texto[::-1]:
        return True
    else:
        return False


TEXTO1 = "anita lava la tina"
print(es_palindromoV2(TEXTO1))  # Output: True

TEXTO2 = "Hola mundo"
print(es_palindromoV2(TEXTO2))  # Output: False
