import warnings
import matplotlib.pyplot as plt
import numpy as np
warnings.filterwarnings("ignore", category=np.VisibleDeprecationWarning) 
def leer_archivo(nombre_archivo):
    """
    Lee un archivo y devuelve una lista con las lineas del archivo
    """
    Archivo = open(nombre_archivo, "r", encoding="utf-8")
    #separar el archivo en una lista de lineas
    lineas = Archivo.readlines()
    #split para separar las lineas en una lista de palabras
    palabras = []
    for linea in lineas:
        ##quitar saltos de linea
        linea = linea.strip()
        palabras.append(linea.split(","))
    return palabras
def obtener_listado_mensual(lista,mes,anio):
    #el formato de fechas es YYYY-MM-DD hh:mm:ss
    #crear una lista con las canciones por mes y anio
    lista_canciones = []
    for i in lista:
        if i[0][5:7] == mes and i[0][:4] == anio:
            lista_canciones.append(i)
            print(i)
    return lista_canciones

def generar_top_10_generos_escuchados(listado_mensual,mes,anio):
    #crear una lista con los generos mas escuchados
    lista_generos = []
    for i in listado_mensual:
        if i[1] not in lista_generos:
            lista_generos.append(i[1])
            print(i)
    #contar las veces que se repite cada artista
    lista_generos_contador = []
    for i in lista_generos:
        contador = 0
        for j in listado_mensual:
            if i == j[1]:
                contador += 1
        lista_generos_contador.append(contador)
    tiempo_generos = []
    for i in range(len(lista_generos)):
        tiempo_generos.append([lista_generos[i],lista_generos_contador[i]])
    #ordenar la lista de mayor a menor con el metodo de burbuja
    for i in range(len(tiempo_generos)-1,0,-1):
        for j in range(i):
            if tiempo_generos[j][1] < tiempo_generos[j+1][1]:
                temp = tiempo_generos[j]
                tiempo_generos[j] = tiempo_generos[j+1]
                tiempo_generos[j+1] = temp
    #crear un archivo de texto con los generos mas escuchados
    #valida si el arreglo tiene elementos
    if len(tiempo_generos) > 0:
        crea_archivo_texto(tiempo_generos[:10],mes,anio)
    else:
        print("No hay elementos en la lista")
    return tiempo_generos


def crea_archivo_texto(lista_generos,mes,anio):
    #crear un archivo de texto con los generos mas escuchados
    Archivo = open("top_10_"+ anio+"_"+ mes+".txt", "w", encoding="utf-8")
    for i in lista_generos:
        Archivo.write(str(i[0]) + "," + str(i[1]) + "\n")
    Archivo.close()

def obtener_minutos_por_genero(listado_mensual,genero):
    #crear una lista con la cantidad de minutos por genero
    lista_minutos = []
    for i in listado_mensual:
        if i[-2] == genero:
            lista_minutos.append(i[-1])
    return lista_minutos
"""
def grafico_minutos_por_genero_mensual(listado_mensual):
        import matplotlib.pyplot as plt
        #crear una lista con todos los generos
        lista_generos = []
        for j in listado_mensual:
            if j[-2] not in lista_generos:
                lista_generos.append(j[-2])
        #crear una lista con la cantidad de minutos por genero
        lista_minutos = []
        for i in lista_generos:
            lista_minutos.append(obtener_minutos_por_genero(listado_mensual,i))
        #suma todos los minutos de la lista de listas de minutos
        plt.bar(lista_generos,lista_minutos,width=0.5)
        plt.xticks(rotation=90)
        plt.title("Generos escuchados")
        plt.xlabel("Generos")
        plt.ylabel("Tiempo escuchados")
        return [lista_generos,lista_minutos]
"""
def crea_grafico_barras_mensual(listado_mensual):
    #crear un grafico de barras con los generos mas escuchados
    #crear una lista con los generos mas escuchados
    lista_generos = []
    for i in listado_mensual:
        if i[1] not in lista_generos:
            lista_generos.append(i[1])
    #contar las veces que se repite cada artista
    lista_generos_contador = []
    for i in lista_generos:
        contador = 0
        for j in listado_mensual:
            if i == j[1]:
                contador += 1
        lista_generos_contador.append(contador)
    #ordenar la lista de mayor a menor con el metodo de burbuja
    for i in range(len(lista_generos_contador)-1,0,-1):
        for j in range(i):
            if lista_generos_contador[j] < lista_generos_contador[j+1]:
                temp = lista_generos_contador[j]
                lista_generos_contador[j] = lista_generos_contador[j+1]
                lista_generos_contador[j+1] = temp
                temp = lista_generos[j]
                lista_generos[j] = lista_generos[j+1]
                lista_generos[j+1] = temp
    #crear una lista con los datos para crear el grafico de barras
    tiempo_generos = []
    for i in range(len(lista_generos)):
        tiempo_generos.append([lista_generos[i],lista_generos_contador[i]])
    #crear el grafico de barras
    import matplotlib.pyplot as plt
    plt.bar(lista_generos,lista_generos_contador,width=0.5)
    plt.xticks(rotation=90)
    plt.title("Top 10 Generos escuchados")
    plt.xlabel("Generos")
    plt.ylabel("Cantidad de veces escuchados")
    plt.show()
    pass



usuario = input("Ingrese el usuario: ")
mes = input("Ingrese el mes: ")
anio = input("Ingrese el año: ")


lista = leer_archivo(usuario)

listado_mensual = obtener_listado_mensual(lista,mes,anio)

generar_top_10_generos_escuchados(listado_mensual,mes,anio)