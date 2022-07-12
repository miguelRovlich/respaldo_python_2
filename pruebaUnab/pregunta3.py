def calcular_tiempo(hora_inicial,minuto_inicial,segundo_inicial,hora_final,minuto_final,segundo_final):
    tiempo_inicial = hora_inicial*3600 + minuto_inicial*60 + segundo_inicial
    tiempo_final = hora_final*3600 + minuto_final*60 + segundo_final
    tiempo_total = tiempo_final - tiempo_inicial
    return tiempo_total

def calcular_velocidad(distancia,tiempo):
    velocidad = distancia/tiempo*60
    return velocidad

puntos_control = open("puntos_control.csv", "r")
pilotos = open("pilotos.csv", "r")

lista_pilotos = []

lista_puntos_control = []

for linea in pilotos:
    linea = linea.strip()
    linea = linea.split(",")
    diccionario = {"punto_control": linea[0], "nombre": linea[1], "tiempo": int(linea[2])}
    lista_pilotos.append(diccionario)

for linea in puntos_control:
    linea = linea.strip()
    linea = linea.split(",")
    diccionario = {"nombre": linea[0], "distancia": int(linea[1])}
    lista_puntos_control.append(diccionario)



#obtener todos los nombres de los pilotos
nombres_pilotos = []
for diccionario in lista_pilotos:
    nombres_pilotos.append(diccionario["nombre"])


#por cada piloto, sumar el tiempo total de todas las etapas
tiempo_total_pilotos = []
for nombre in nombres_pilotos:
    tiempo_total = 0
    for diccionario in lista_pilotos:
        if diccionario["nombre"] == nombre:
            tiempo_total += diccionario["tiempo"]
    tiempo_total_pilotos.append([nombre,tiempo_total])

print("Piloto ganador fue: ", min(tiempo_total_pilotos, key=lambda x: x[0]))




archivo_mas_rapido = open("mas_rapido.csv", "w")

for punto in lista_puntos_control:
    velocidad_mayor = 0
    piloto_mas_rapido = ""
    for piloto in lista_pilotos:
        if piloto["punto_control"] == punto["nombre"]:
            velocidad_piloto = calcular_velocidad(punto["distancia"], piloto["tiempo"])
            print("Piloto: ", piloto["nombre"], "Velocidad: ", velocidad_piloto)
            if velocidad_piloto > velocidad_mayor:
                velocidad_mayor = velocidad_piloto
                piloto_mas_rapido = piloto["nombre"]
    archivo_mas_rapido.write( punto["nombre"]+ "," +piloto_mas_rapido+ "\n")

archivo_velocidad_promedio = open("velocidad_pilotos.csv", "w")
for piloto in lista_pilotos:
    velocidad_promedio = 0
    for punto in lista_puntos_control:
        if piloto["punto_control"] == punto["nombre"]:
            velocidad_promedio += calcular_velocidad(punto["distancia"], piloto["tiempo"])
    velocidad_promedio = velocidad_promedio/len(lista_puntos_control)
    archivo_velocidad_promedio.write( piloto["nombre"]+ "," +str(velocidad_promedio)+ "\n")


archivo_velocidad_etapa = open("velocidad_etapa.csv", "w")
for punto in lista_puntos_control:
    velocidad_promedio = 0
    for piloto in lista_pilotos:
        if piloto["punto_control"] == punto["nombre"]:
            velocidad_promedio += calcular_velocidad(punto["distancia"], piloto["tiempo"])
    velocidad_promedio = velocidad_promedio/len(lista_pilotos)
    archivo_velocidad_etapa.write( punto["nombre"]+ "," +str(velocidad_promedio)+ "\n")



archivo_tiempo_total = open("tiempo_total.csv", "r")

lista_tiempos = []

for tiempo in archivo_tiempo_total:
    tiempo = tiempo.strip()
    tiempo = tiempo.split(",")
    diccionario = {"nombre": tiempo[0], "tiempo": int(tiempo[1])}
    lista_tiempos.append(diccionario)

for i in lista_tiempos:
    for j in lista_tiempos:
        if i["nombre"] == j["nombre"]:
            i["tiempo"] += j["tiempo"]

print(lista_tiempos)
