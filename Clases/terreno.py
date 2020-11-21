from .condominio import condominio

class Terreno:
   # Definicion de contructor de inicializacion
    def __init__ (self, arg1, arg2, arg3, arg4, arg5, arg6):
        self.superficie = arg1
        self.tierra = arg2
        self.piedras = arg3
        self.arboles = arg4
        self.pasto = arg5
        self.grama = arg6

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

