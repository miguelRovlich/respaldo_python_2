def agregarJefe(lista, jefe):
    lista.append(jefe)
    return lista

def eliminarJefe(lista, jefe):
    lista.remove(jefe)
    return lista

def agregarProducto(lista, producto):
    lista.append(producto)
    return lista

def eliminarProducto(lista, producto):
    lista.append(producto)
    return lista

jefes = open("jefes.txt", "r")
listaJefes = []
for linea in jefes:
    listaJefes = agregarJefe(listaJefes, linea)
productos = open("productos.txt", "r")
listaProductos = []
for linea in productos:
    listaProductos = agregarProducto(listaProductos, linea)
opcion = 0
while opcion != 0:
    print("Opcion 1: Agregar jefe")
    print("Opcion 2: Eliminar jefe")
    print("Opcion 3: Agregar producto")
    print("Opcion 4: Eliminar producto")
    print("Opcion 4: Generar resumen")
    print("Opcion 6: Salir")
    
    opcion = int(input("Ingrese una opcion: "))
    if opcion == 1:
        jefe = input("Ingrese el nombre del jefe: ")
        agregarJefe(jefes, jefe)
    elif opcion == 2:
        jefe = input("Ingrese el nombre del jefe: ")
        eliminarJefe(jefes, jefe)
    elif opcion == 3:
        producto = input("Ingrese el nombre del producto: ")
        agregarProducto(productos, producto)
    elif opcion == 4:
        producto = input("Ingrese el nombre del producto: ")
        eliminarProducto(productos, producto)
    elif opcion == 5:
        print(jefes)
        print(productos)
    elif opcion == 6:
        print("Saliendo...")
        #reescribir archivos
        jefes.close()
        productos.close()
        jefes = open("jefes.txt", "w")
        productos = open("productos.txt", "w")
        for jefe in listaJefes:
            jefes.write(jefe)
        for producto in listaProductos:
            productos.write(producto)
        jefes.close()
        productos.close()
    else:
        print("Opcion incorrecta")



