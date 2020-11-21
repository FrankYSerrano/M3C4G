from .condominio import condominio
from .terreno import Terreno

class CondominioHorizontal (condominio, Terreno):
   # Definicion de contructor de inicializacion
    def __init__(self, plaza, piscina, estacionamiento, helipuerto, muelle,
                direccion, lista_administrador, lista_guardias, num_unidades_habitacionales, lista_unidades, cuenta_corriente,
                superficie, tierra, piedras, arboles, pasto, grama):
        condominio.__init__(direccion, lista_administrador, lista_guardias, num_unidades_habitacionales, lista_unidades, cuenta_corriente)
        Terreno.__init__(superficie, tierra, piedras, arboles, pasto, grama)
        self.plaza = plaza
        self.piscina = piscina
        self.estacionamiento = estacionamiento
        self.helipuerto = helipuerto
        self.muelle = muelle

        print("Cree instancia de clase CondominioHorizontal")


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

