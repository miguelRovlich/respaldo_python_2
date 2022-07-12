temperatura = 0
temperatura_maxima = -200
temperatura_minima = 200
suma_temperaturas = 0
contador_temperaturas = 0
while temperatura != -100:
    temperatura = int(input("Ingrese temperatura: "))
    if temperatura >= -30 and temperatura <= 45:
        if temperatura > temperatura_maxima:
            temperatura_maxima = temperatura
        if temperatura < temperatura_minima:
            temperatura_minima = temperatura
        suma_temperaturas += temperatura
        contador_temperaturas += 1
    else:
        print("Temperatura fuera de rango")
promedio_temperaturas = suma_temperaturas / contador_temperaturas
print("Temperatura máxima: ", temperatura_maxima)
print("Temperatura mínima: ", temperatura_minima)
print("Promedio de temperaturas: ", promedio_temperaturas)

