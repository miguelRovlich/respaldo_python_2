class Carta:
    def __init__(self,tipo,color):
        self.tipo = tipo
        self.color = color
    def __str__(self):
        return self.tipo + self.color
class Cuerpo:
    def __init__(self,cartas_amarillas,cartas_rojas,cartas_azules):
        self.cartas_amarillas = cartas_amarillas
        self.cartas_rojas = cartas_rojas
        self.cartas_azules = cartas_azules
    def agregar_carta_cuerpo(self,carta):
        if carta.color == "roja":
            self.cartas_rojas.append(carta)
        elif carta.color == "azul":
            self.cartas_azules.append(carta)
        elif carta.color == "amarilla":
            self.cartas_amarillas.append(carta)
        else:
            print("la carta no es valida")
    def esta_completo_y_sano(self):
        #recorre las cartas del cuerpo y verifica que no haya cartas de tipo virus
        organos_rojos = 0
        organos_azules = 0
        organos_amarillos = 0
        for carta in self.cartas_rojas:
            if carta.tipo == "virus":
                return False
            if carta.tipo == "organo":
                organos_rojos += 1
        for carta in self.cartas_azules:
            if carta.tipo == "virus":
                return False
            if carta.tipo == "organo":
                organos_azules += 1
        for carta in self.cartas_amarillas:
            if carta.tipo == "virus":
                return False
            if carta.tipo == "organo":
                organos_amarillos += 1
        #si hay uno o mas organos en cada color, entonces el cuerpo esta completo y sano
        if organos_rojos == 1 and organos_azules == 1 and organos_amarillos == 1:
            return True
        else:
            return False
    def __str__(self):
        if self.esta_completo_y_sano():
            return "El cuerpo esta sano"
        else:
            return "El cuerpo no esta sano o le faltan organos"

class Jugador:
    def __init__(self, nombre, cuerpo, mano):
        self.nombre = nombre
        self.cuerpo = cuerpo
        self.mano = mano
    def descartar_cartas(self,nueva_mano):
        self.mano = nueva_mano
    def bajar_cartas(self,carta):
        self.cuerpo.agregar_carta_cuerpo(carta)
    def agregar_carta_mano(self,carta):
        self.mano.append(carta)
    def eliminar_carta_mano(self,carta):
        self.mano.remove(carta)
    def __str__(self):
        return "Jugador(a)" + self.nombre

#inicio del programa
#pedir 3 nombres de jugadores
nombre_jugador_1 = input("ingrese el nombre del jugador 1: ")
nombre_jugador_2 = input("ingrese el nombre del jugador 2: ")
nombre_jugador_3 = input("ingrese el nombre del jugador 3: ")
#recibir las cartas de cada jugador
cartas_jugador_1 = input("ingrese cartas del jugador 1: ").split(";")
cartas_jugador_2 = input("ingrese cartas del jugador 2: ").split(";")
cartas_jugador_3 = input("ingrese cartas del jugador 3: ").split(";")
#empieza el juego
cuerpo = Cuerpo([],[],[])
jugador_1 = Jugador(nombre_jugador_1,cuerpo,[])
jugador_2 = Jugador(nombre_jugador_2,cuerpo,[])
jugador_3 = Jugador(nombre_jugador_3,cuerpo,[])

#preguntar si el jugador quiere jugar carta o descartar cartas
opcion_carta = input("ingrese una opcion: (jugar carta/descartar cartas)")
if opcion_carta == "jugar carta":
    indice_carta = int(input("ingrese el indice de la carta que desea jugar: "))
    carta_jugada = jugador_1.mano[indice_carta]
elif opcion_carta == "descartar cartas":
    nueva_mano = input("ingrese nuevas cartas del jugador: ").split(";")
    jugador_1.descartar_cartas(nueva_mano)