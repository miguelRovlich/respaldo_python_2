#abrir archivo de ingredientes
Archivo = open('ingredientes.txt','r')

ing = {}
#recorrer el archivo y generar el diccionario de ingredientes
for linea in Archivo:
    a = linea.split(" ")
    ingrediente = a[0]
    cantidad = int(a[1].rstrip())
    ing[ingrediente] = cantidad

Archivo2 = open('recetas.csv','r')
recetas = {}
#generar el dicionario de recetas
for linea2 in Archivo2:
    a2 = linea2.split(",")
    nombre = a2[0]
    listaIngredientes = []
    for i in range(1,len(a2)):
        if i == len(a2) -1:
            #sacar el \n del ultimo item
            rstrip = a2[i].rstrip()
            listaIngredientes.append(rstrip)
        else:
            listaIngredientes.append(a2[i])

    recetas[nombre] = listaIngredientes

opcion = ''
while opcion != "STOP":
    
    print("")
    
    print('Stock actual de ingredientes disponibles')
    listado = list(ing.keys())
    for j in listado:
        getter = ing.get(j)
        print(j,": ",getter)
    print()
    opcion = input('Ingrese opcion: Ingresa la receta que quieres o REPONER: ')
    #transformo el texto en una lista
    opt = opcion.split(' ')
    if opt[0] == 'PREPARAR':
        #borrado del preparar
        opt.pop(0)

        #comprobando que la receta exista
        if opt[0] not in recetas:
            print('Lo siento, no preparamos ',opt[0])
        else:
            lista = recetas[opt[0]]
            key2 = []
            for key in lista:
                if key in ing:
                    arr = ing[key]
                    if arr == 0:
                        print('No podemos preparar la receta porque falta: ',key)
                        break
                    else:
                        arr = arr - 1
                        key2.append(arr)
                        ing[key] = arr
            print('Plato Finalizado')
            print()   
    elif opt[0] =='REPONER':
        opt.pop(0)
        lista = opt
        print (lista)
        #recorriendo la lista generada y sumando 1 en caso de que exista
        for i in lista:
            if i in ing:
                arr = ing[i]
                print(arr)
                arr = arr + 1
                ing[i] = arr
    elif opt[0] =="STOP":
        print("Fin del programa")
    else:   
        print('Error, opcion invalida')