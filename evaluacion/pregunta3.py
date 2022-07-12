import random 

#generar una matriz de n x m con numeros aleatorios del 0 al 20
n = int(input("ingrese el numero de filas: "))
m = int(input("ingrese el numero de columnas: "))
matriz = []
for i in range(n):
    matriz.append([])
    for j in range(m):
        matriz[i].append(random.randint(0,20))
#imprimir matriz en forma de tabla sin bordes
for i in range(n):
    for j in range(m):
        print(matriz[i][j],end=" ")
    print()
#guardar la matriz en un archivo de texto
archivo = open("matriz_"+str(n)+"_por_"+str(m)+".txt","w")
for i in range(n):
    for j in range(m):
        archivo.write(str(matriz[i][j]) + " ")
    archivo.write("\n")
archivo.close()


print("lectura archivo")
#leer la matriz del archivo de texto
archivo = open("matriz_"+str(n)+"_por_"+str(m)+".txt","r")
matriz = []
#quitar salto de linea al final de cada linea
for linea in archivo:
    linea = linea.rstrip()
    matriz.append(linea.split())

#imprimir matriz en forma de tabla sin bordes
for i in range(n):
    for j in range(m):
        print(matriz[i][j],end=" ")
    print()