"""Función para contar vocales"""
def vocales(frase):
    contador = 0
    lista = ["a", "e", "i", "o", "u"]
    for vocal in frase:
        if vocal in lista:
            contador = contador + 1
    return contador

"""Función dados"""
def dados():
    import random
    n = random.randint(1, 6)
    return f"El número que ha salido ha sido: {n}"
