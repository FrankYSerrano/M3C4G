import Clases as C

# Lista de Administradores. SERIA IDEAL UNA CLASE ADMINISTRADORES
admins_A = ['Felipe', 'Guido', 'Cristian', 'Fernando', 'Frank']
admins_B = ['Guido', 'Cristian', 'Fernando']

#Creacion de Guardias. SERIA IDEAL UNA CLASE HERRAMIENTAS CON uuid UNICO
herram_basicas = ['Llaves', 'Linterna', 'Llave para ascensor']
herram_avanzadas = ['Pistola', 'Chaleco', 'Impermeable', 'Llaves', 'Linterna', 'Llave para ascensor']
Guard01 = C.Guardia("Azul", herram_basicas, "Flaco")
Guard02 = C.Guardia("Verde", herram_avanzadas, "Corpulento")
Guard03 = C.Guardia("Azul", herram_basicas, "Flaco")
Guard04 = C.Guardia("Verde", herram_avanzadas, "Gordo")
Guard05 = C.Guardia("Rojo", herram_avanzadas, "Schwarzenegger")

#Creacion de Listas de Guardias
guardias_A = [Guard01, Guard02, Guard03, Guard04, Guard05]
guardias_B = [Guard02, Guard04, Guard05]

#Creacion de lista de Unidades para cada conjunto
L_Unidades1 =['01', '02', '03', '04', '05']
L_Unidades2 =['01', '02', '03', '04', '05', '06', '07', '08', '09', '10']

#Creacion de cuentas corrientes
cc1 = C.CuentaCorriente(100000, 2000000, 15000)
cc2 = C.CuentaCorriente(500000, 3000000, 5000)

#Creacion de Terrenos
Terr1 = C.Terreno (100, "negra", "muchas", 0, "siboulette", "artificial")
Terr2 = C.Terreno (300, "playa", "ninguna", 5, "lechuga", "natural")

#Creacion de conjuntos de casas. VALIDAR LO ASOCIADO A TERRENO PARA QUE EXISTE ESA CLASE VS ESTOS PARAMETROS
conj1 = C.CondominioHorizontal(1, 2, 30, 1, 1, "DirConj1",admins_A, guardias_A, 5, L_Unidades1, cc1, 100, "negra", "muchas", 0, "siboulette", "artificial")
conj2 = C.CondominioHorizontal(2, 1, 10, 0, 0, "DirConj2",admins_B, guardias_B, 10, L_Unidades2, cc2, 300, "playa", "ninguna", 5, "lechuga", "natural")

