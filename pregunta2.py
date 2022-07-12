ingreso_total = int(input("Ingrese los ingresos del hogar: "))
cantidad_personas = int(input("ingrese la cantidad de personas: "))
tercera_edad = int(input("cuantas personas son tercera edad?: "))


def hasta_4_personas(tercera_edad,ingreso_per_capita):
    if tercera_edad >= 2:
        print("El hogar es C3")
    else:
        if ingreso_per_capita <= 60000:
            print("El hogar es C3")
        elif ingreso_per_capita > 60000 and ingreso_per_capita <= 100000:
            print("El hogar es C2")
        elif ingreso_per_capita > 100000 and ingreso_per_capita <= 300000:
            print("El hogar es C1")
        elif ingreso_per_capita > 300000:
            print("El hogar es AB")

def mas_de_4_personas(tercera_edad,ingreso_per_capita):
    if tercera_edad >= 2:
        print("El hogar es C3")
    else:
        if ingreso_per_capita <= 40000:
            print("El hogar es C3")
        elif ingreso_per_capita > 40000 and ingreso_per_capita <= 80000:
            print("El hogar es C2")
        elif ingreso_per_capita > 80000 and ingreso_per_capita <= 250000:
            print("El hogar es C1")
        elif ingreso_per_capita > 250000:
            print("El hogar es AB")


if tercera_edad > cantidad_personas:
    print("Error")
    exit()
else:
    ingreso_per_capita = ingreso_total / cantidad_personas
    if cantidad_personas <= 4:
        hasta_4_personas(tercera_edad,ingreso_per_capita)
    else:
        mas_de_4_personas(tercera_edad,ingreso_per_capita)

