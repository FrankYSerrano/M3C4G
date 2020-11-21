from .condominio import condominio
class CuentaCorriente:
   # Definicion de contructor de inicializacion
    def __init__ (self, estado_cuenta, saldo, giro):
        self.estado_cuenta = estado_cuenta
        self.saldo = saldo
        self.giro = giro

        print("Cree instancia de clase CuentaCorriente")

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
