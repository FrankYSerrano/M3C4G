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
Casa_01 = C.UnidadHabitacional(True, 3, True)
Casa_02 = C.UnidadHabitacional(False, 5, False)
Casa_03 = C.UnidadHabitacional(True, 8, False)
Casa_11 = C.UnidadHabitacional(True, 3, True)
Casa_12 = C.UnidadHabitacional(True, 4, False)
Casa_13 = C.UnidadHabitacional(True, 6, True)
Casa_14 = C.UnidadHabitacional(True, 10, False)
Casa_15 = C.UnidadHabitacional(True, 1, True)
Casa_16 = C.UnidadHabitacional(True, 3, True)
L_Casas_1 =[Casa_01, Casa_02, Casa_03]
L_Casas_2 =[Casa_11, Casa_12, Casa_13, Casa_14, Casa_15, Casa_16]

#Creacion de cuentas corrientes
cc1 = C.CuentaCorriente(100000, 2000000, 15000)
cc2 = C.CuentaCorriente(500000, 3000000, 5000)

#Creacion de Terrenos
Terr1 = C.Terreno (100, "negra", "muchas", 0, "siboulette", "artificial")
Terr2 = C.Terreno (300, "playa", "ninguna", 5, "lechuga", "natural")

#Creacion de conjuntos de casas.
conj1 = C.CondominioHorizontal(1, 2, 30, 1, 1, "DirConj1", admins_A, guardias_A, len(L_Casas_1), L_Casas_1, cc1, Terr1)
conj2 = C.CondominioHorizontal(2, 1, 10, 0, 0, "DirConj2", admins_B, guardias_B, len(L_Casas_2), L_Casas_2, cc2, Terr2)

#print(conj1.num_unidades_habitacionales)
#print(conj2.num_unidades_habitacionales)

#Creacion de conjuntos de edificios.

