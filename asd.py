lista = []
palabra = input('Escribe una palabra: ')


#agregar cada letra de la palabra a la lista
for letra in palabra:
    lista.append(letra)
lista_desplegable = ""
for letra in lista:
    lista_desplegable.append("*")

print(lista_desplegable)
print(lista)