from .condominio import condominio
class UnidadHabitacional:
   # Definicion de contructor de inicializacion
    def __init__ (self, arg1, arg2, arg3):
        self.puerta = arg1
        self.ventanas = arg2
        self.techo = arg3

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

