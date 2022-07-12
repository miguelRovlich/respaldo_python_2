class Etapa:
    def __init__(self, nombre, distancia):
        self.nombre = nombre
        self.distancia = distancia
    
class Piloto:
    def __init__(self, nombre,punto_control,tiempo):
        self.nombre = nombre
        self.punto_control = punto_control
        self.tiempo = tiempo
    def calcular_tiempo_total(hora_entrada,minuto_entrada,segundo_entrada,hora_salida,minuto_salida,segundo_salida):
        pass
    def calcular_velocidad(distancia,tiempo):
        pass
    def calcular_piloto_mas_rapido(pilotos):
        pass
    def velocidad_promedio_piloto(pilotos):
        pass
    def piloto_ganddor(pilotos):
        pass
    def velocidad_promedio_etapa(etapas,pilotos):
        pass
    