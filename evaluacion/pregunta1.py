vocales = "aeiou"
lista = []
palabras = ""
while palabras != "end":
    palabras = input("Ingrese una palabra: ")
    if palabras == "end":
        break
    lista.append(palabras)
excepciones = ["ee", "oo", "rr", "ll"]
for i in lista:
    cantidad_vocales = 0
    # revisar si la palabra tiene vocales
    for letra in i:
        if letra in vocales:
            cantidad_vocales += 1
    if cantidad_vocales > 0:
        # revisar si hay espacios 
        if " " not in i:
            # revisar que no existan caracteres repetidos salvo las excepciones
           for j in range(len(i) -1):
                tramo = i[j]+i[j+1] # estas son las dos letras que se van a comparar y se requieren unidas para comparar con excepciones
                if i[j] != i[j + 1] or tramo in excepciones:
                    #revisar si la palabra solo tiene letras
                    if i.isalpha():
                        print("aceptable")
                        break
                    else:
                        print("no aceptable")
                        break
                else:
                    print("existen caracteres repetidos")
        else:
            print("tiene espacios")
    else:
        print("no tiene vocales")

