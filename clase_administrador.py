#Clase Administrador con atributos privados, getters y setters

class Administrador:
    def __init__(self, vidas) -> None:
        self.__vidas = vidas
        self.__tiempo = 0
        self.__nivel = 1
        self.__score = 0
        self.__nombre_jugador = ""

    @property
    def vidas(self)->object:
        return self.__vidas    
    @vidas.setter
    def vidas(self, nuevas_vidas)->None:
        self.__vidas = nuevas_vidas

    @property
    def tiempo(self):
        return self.__tiempo
    @tiempo.setter
    def tiempo(self, nuevo_tiempo):
        self.__tiempo = nuevo_tiempo

    @property
    def nivel(self)->object:
        return self.__nivel    
    @nivel.setter
    def nivel(self, nuevo_nivel)->None:
        self.__nivel = nuevo_nivel
    
    @property
    def score(self):
        return self.__score
    @score.setter
    def score(self, nuevo_score):
        self.__score = nuevo_score

    @property
    def nombre_jugador(self):
        return self.__nombre_jugador
    @nombre_jugador.setter
    def nombre_jugador(self, nuevo_nombre):
        self.__nombre_jugador = nuevo_nombre
