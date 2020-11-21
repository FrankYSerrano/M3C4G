# Definicion de Clase
class Guardia:
   # Definicion de contructor de inicializacion
    def __init__ (self, arg1, arg2, arg3):
        self.Uniforme = arg1
        self.Herramientas = arg2
        self.a3 = arg3

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

class CuentaCorriente:
   # Definicion de contructor de inicializacion
    def __init__ (self, arg1, arg2, arg3):
        self.estado_cuenta = arg1
        self.saldo = arg2
        self.giro = arg3

   # Definicion de metodo 1
    def girar(self):
        print("Clase CtaCorr - Metodo 1") 

   # Definicion de metodo 2
    def abonar(self):
        print("Clase CtaCorr - Metodo 2") 

   # Definicion de metodo 3
    def bloquear(self):
        print("Clase CtaCorr - Metodo 3") 

   # Definicion de metodo 4
    def desbloquear(self):
        print("Clase CtaCorr - Metodo 4") 

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

class CondominoVertical:
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

class CondominioHorizontal:
   # Definicion de contructor de inicializacion
    def __init__ (self, arg1, arg2, arg3, arg4, arg5):
        self.plaza = arg1
        self.piscina = arg2
        self.estacionamiento = arg3
        self.helipuerto = arg4
        self.muelle = arg5

   # Definicion de metodo 1  POLIFORMICO!!!
    def construir_casa(self):
        print("Clase CondHoriz - Metodo 1") 

   # Definicion de metodo 2
    def limpiar_plaza(self):
        print("Clase CondHoriz - Metodo 2") 

   # Definicion de metodo 3
    def limpiar_piscina(self):
        print("Clase CondHoriz - Metodo 3") 

   # Definicion de metodo 4
    def limpiar_estacionamiento(self):
        print("Clase CondHoriz - Metodo 5") 

   # Definicion de metodo 5
    def limpiar_helipuerto(self):
        print("Clase CondHoriz - Metodo 5") 

   # Definicion de metodo 6
    def limpiar_muelle(self):
        print("Clase CondHoriz - Metodo 6") 

