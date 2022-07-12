presion_minima = 49.03
n = int(input("Ingrese número de mediciones a realizar: "))
n_deficientes = 0
suma = 0
contador = 0
while contador < n:
    presion = float(input("Ingrese presión: "))
    if presion < presion_minima:
        n_deficientes += 1
        print("Presión deficiente")
    suma += presion
    contador += 1
promedio = suma / n
if n_deficientes > n/2:
    print("La muestra esta fuera de ley")
    print("Hay más de la mitad de mediciones con presiones deficientes")
elif promedio < presion_minima:
    print("La muestra esta fuera de ley")
    print("La presión promedio es menor a la presión mínima")
else:
    print("La muestra esta dentro de ley")
