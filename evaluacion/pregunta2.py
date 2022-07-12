### las 


lista_origen  = ["Santiago","Concepcion","Temuco","Valdivia","Osorno","Puerto Montt"]
lista_destino = ["Santiago","Concepcion","Temuco","Valdivia","Osorno","Puerto Montt"]
viajes = []
opcion = -1
while opcion != 0:
    print("1. Venta de pasajes")
    print("2. Reporte de pasajes vendidos")
    print("3. Salir")
    opcion = int(input("Ingrese una opcion: "))
    if opcion == 1:
        nombre = input("Ingrese su nombre: ")
        apellido = input("Ingrese su apellido: ")
        fecha_nacimiento = input("Ingrese su fecha de nacimiento: ")
        #imprimir ciudades de origen
        print("Ciudades de origen: ")
        for i in range(len(lista_origen)):
            print(i+1,lista_origen[i])
        ciudad_origen = input("Ingrese su ciudad de origen: ")
        #imprimir ciudades de destino
        print("Ciudades de destino: ")
        for i in range(len(lista_destino)):
            print(i+1,lista_destino[i])
        ciudad_destino = input("Ingrese su ciudad de destino: ")
        #validar que las ciudades de origen y destino sean distintas
        while ciudad_origen == ciudad_destino:
            print("Las ciudades de origen y destino deben ser distintas")
            print("Ciudades de destino: ")
            for i in range(len(lista_destino)):
                print(i+1,lista_destino[i])
            ciudad_destino = input("Ingrese su ciudad de destino: ")
        fecha = input("Ingrese la fecha de viaje: ")
        hora = input("Ingrese la hora de viaje: ")
        #crear un diccionario con los datos del viaje
        viaje = {
            "nombre":nombre,
            "apellido":apellido,
            "fecha_nacimiento":fecha_nacimiento,
            "ciudad_origen":ciudad_origen,
            "ciudad_destino":ciudad_destino,
            "fecha":fecha,
            "hora":hora
        }
        #agregar el viaje a la lista de viajes
        viajes.append(viaje)
        #guardar la lista de viajes en un archivo de texto
        archivo = open("viajes.txt","w")
        for i in range(len(viajes)):
            archivo.write(str(viajes[i]) + "\n")
        archivo.close()
    elif opcion == 2:
        if len(viajes) == 0:
            print("No hay viajes registrados")
        else:
            #imprimir los viajes
            print("Viajes: ")
            for i in range(len(viajes)):
                print(i+1,viajes[i])
            #imprimir la cantidad de viajes
            print("Cantidad de viajes: ",len(viajes))
            #consultar el detalle de un viaje
            opcion = int(input("Ingrese el numero de viaje: "))
            print("Nombre: ",viajes[opcion-1]["nombre"])
            print("Apellido: ",viajes[opcion-1]["apellido"])
            print("Fecha de nacimiento: ",viajes[opcion-1]["fecha_nacimiento"])
            print("Ciudad de origen: ",viajes[opcion-1]["ciudad_origen"])
            print("Ciudad de destino: ",viajes[opcion-1]["ciudad_destino"])
            print("Fecha: ",viajes[opcion-1]["fecha"])
            print("Hora: ",viajes[opcion-1]["hora"])
    elif opcion == 3:
        print("Gracias por usar el programa")
    else:
        print("Opcion no valida")
        opcion = -1
        continue
