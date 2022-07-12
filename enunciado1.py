def contarLetras(cadena, letra):
    contador = 0
    for i in cadena:
        if i == letra:
            contador += 1
    return contador

print(contarLetras("Hola mundo", "o"))
