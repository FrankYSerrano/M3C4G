from .condominio import condominio
from .terreno import Terreno

class CondominoVertical (condominio, Terreno):
   # Definicion de contructor de inicializacion
    def __init__ (self, arg1, arg2, arg3, arg4, arg5):
        self.num_de_pisos = arg1
        self.num_de_ascensores = arg2
        self.escaleras = arg3
        self.entrada = arg4
        self.color = arg5

   # Definicion de metodo 1 POLIFORMICO!!!
    def construir_edificio(self):
        print("Clase CondVert - Metodo 1") 

   # Definicion de metodo 2
    def limpiar_piso(self):
        print("Clase CondVert - Metodo 2") 

   # Definicion de metodo 3
    def limpiar_piscina(self):
        print("Clase CondVert - Metodo 3") 

   # Definicion de metodo 4
    def limpiar_ascensor(self):
        print("Clase CondVert - Metodo 4") 

   # Definicion de metodo 5
    def limpiar_escaleras(self):
        print("Clase CondVert - Metodo 5") 

   # Definicion de metodo 6
    def limpiar_entrada(self):
        print("Clase CondVert - Metodo 6") 
