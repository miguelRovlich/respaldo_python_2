
def agregarPatentes(lista,n):
    for i in range(n):
        patente = input("Ingrese patente: ")
        lista.append(patente)
    return lista

def buscarRestriccion(lista,digito1,digito2):
    nuevaLista = []
    for i in lista:
        if int(i[-1])  == digito1 and int(i[-2]) == digito2:
            nuevaLista.append(i)
    return nuevaLista

#programa principal
lista = []
n = int(input("Ingrese cantidad de patentes: "))
lista = agregarPatentes(lista,n)
digito1 = int(input("Ingrese digito 1: "))
digito2 = int(input("Ingrese digito 2: "))
lista = buscarRestriccion(lista,digito1,digito2)
print(lista)
