from .condominio import condominio
class UnidadHabitacional:
   # Definicion de contructor de inicializacion
    def __init__ (self, puerta, ventanas, techo):
        self.puerta = puerta
        self.ventanas = ventanas
        self.techo = techo

   # Definicion de metodo 1
    def abrir_puerta(self):
        print("Clase UnidadHab1 - Metodo 1") 

   # Definicion de metodo 2
    def abrir_llave_agua(self):
        print("Clase UnidadHab1 - Metodo 2") 

   # Definicion de metodo 3
    def cerrar_puerta(self):
        print("Clase UnidadHab1 - Metodo 3") 

   # Definicion de metodo 4
    def encender_luz(self):
        print("Clase UnidadHab1 - Metodo 4") 

