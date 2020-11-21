from .condominio import condominio

class Terreno:
   # Definicion de contructor de inicializacion
    def __init__ (self, superficie, tierra, piedras, arboles, pasto, grama):
        self.superficie = superficie
        self.tierra = tierra
        self.piedras = piedras
        self.arboles = arboles
        self.pasto = pasto
        self.grama = grama

        print("Cree instancia de clase Terreno ", self.superficie)

   # Definicion de metodo 1
    def construir_casa(self):
        print("Clase Terreno - Metodo 1") 

   # Definicion de metodo 2
    def construir_edificio(self):
        print("Clase Terreno - Metodo 2") 

   # Definicion de metodo 3
    def construir_estacionamiento(self):
        print("Clase Terreno - Metodo 3") 

   # Definicion de metodo 4
    def construir_piscina(self):
        print("Clase Terreno - Metodo 4") 

   # Definicion de metodo 5
    def construir_plaza(self):
        print("Clase Terreno - Metodo 5") 

   # Definicion de metodo 6
    def construir_caseta(self):
        print("Clase Terreno - Metodo 6") 

