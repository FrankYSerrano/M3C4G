#from  .guardia import Guardia

class  condominio:
    def __init__(self, direccion, lista_administrador, lista_guardias, num_unidades_habitacionales,
                lista_unidades, cuenta_corriente):
            self.direccion = direccion
            self.lista_administrador = lista_administrador
            self.lista_guardias = lista_guardias
            self.num_unidades_habitacionales = num_unidades_habitacionales
            self.lista_unidades = lista_unidades
            self.cuenta_corriente = cuenta_corriente
            self.__pr_enca__= "xxx"
            print("Cree instancia de clase condominio ", self.direccion)

    @property
    def get_direccion(self, direccion):
        self.direccion = direccion 
        return self.direccion

#    @direccion.setter
    def set_direccion(self, direccion):
        print("Aqui muestro el setter")
        self.direccion = direccion

    @property
    def get_administrador(self, administrador):
        self.administrador = administrador
        return self.administrador

#    @administrador.setter
    def set_administrador(self,administrador):
        self.administrador = administrador
 
    def add_guardia(self, guardia):
        self.lista_guardias.append(guardia)
        print("se agragara el guardia ", guardia.corpulencia)
        return self.lista_guardias   

    def del_guardia(self, guardia):
        self.lista_guardias.remove(guardia) 
        print("se removera el guardia ", guardia.corpulencia)
        return self.lista_guardias

    @property
    def get_guardias(self, guardia):
        #super(guardia).__init__(self, "Uniforme", [], "statan")
        self.guardia = guardia
        return self.guardia   

    @property
    def get_unidades(self, lista_unidades):
        self.lista_unidades = lista_unidades
        return self.lista_unidades                 

    def __listar_guardias__(self):
        for guardia in self.lista_guardias:
            print(guardia.corpulencia)

    def metodo2(self):
        print("Metodo 2")

    def metodo3(self):
        print("Metodo 3")

    def metodo4(self):
        print("Metodo 4")

# get_direccion, set_direccion, set_administrador,
# get_administrador, add_guardia, del_guardia, get_guardias,
# get_unidades
# Agregue 4 métodos adicionales que usted considere apropiados
