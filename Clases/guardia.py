from .condominio import condominio

# Definicion de Clase
class Guardia:
   # Definicion de contructor de inicializacion
    def __init__ (self, Uniforme, Herramientas, corpulencia):
        self.Uniforme = Uniforme
        self.Herramientas = Herramientas
        self.corpulencia = corpulencia

        print("Cree instancia de clase Guardia")

   # Definicion de metodo 1
    def patrullaje(self):
        print("Clase Guardia - Metodo 1") 

   # Definicion de metodo 2
    def saludo(self):
        print("Clase Guardia - Metodo 2") 

   # Definicion de metodo 3
    def registro_visitas(self):
        print("Clase Guardia - Metodo 3") 

   # Definicion de metodo 4
    def contar_chismes(self):
        print("Clase Guardia - Metodo 4") 
