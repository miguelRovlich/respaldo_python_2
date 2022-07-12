stock = open("stock.csv", "r")
# Leer el archivo y guardarlo en una lista de diccionarios
lista = []
for linea in stock:
    linea = linea.strip()
    linea = linea.split(",")
    diccionario = {"nombre": linea[0], "cantidad": int(linea[1]), "precio": int(linea[2])}
    lista.append(diccionario)
print(lista)
opcion = 0

while opcion != 2:
    print("1. Revisar producto")
    print("2. Salir")
    opcion = int(input("Ingrese opcion: "))
    if opcion == 1:
        producto_buscado = input("Ingrese producto: ")
        #recolectar todos los precios del producto
        precios = []
        cantidades = []
        for diccionario in lista:
            if diccionario["nombre"] == producto_buscado:
                precios.append(diccionario["precio"])
                cantidades.append(diccionario["cantidad"])
        #sumar todos los precios
        suma = 0
        for i in cantidades :
            suma += i
        #encontrar el precio mas alto
        precio_mas_alto = max(precios)
        print("Precio mas alto: ", precio_mas_alto*1.3)
        print("Stock total: ",suma )
    elif opcion == 2:
        print("Gracias por usar el programa")
    else:
        print("Opcion no valida")
