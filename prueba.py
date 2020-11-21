class Contacto:
    contactos = []
    def __init__(self, nombre, email):
        self.nombre= nombre
        self.email = email
#        Contacto.contactos.append(self)
        self.contactos.append(self)

class Proveedor(Contacto):
    def orden(self, orden):
        print("Si este fuera un sistema real enviariamos la {} orden a {}".format(orden, self.nombre))

c = Contacto("Alguien", "alguien@ejemplo.net")
c2 = Contacto("Alguien2", "alguien2@ejemplo.net")
print(c.contactos)
print(c2.contactos)
p = Proveedor("Proveedor", "prov@ejemplo.net")
p2 = Proveedor("Proveedor2", "prov2@ejemplo.net")
print(c.nombre, c.email, p.nombre, p.email)
#Alguien alguien@ejemplo.net Pro veedor prov@ejemplo.net
print(c.contactos)
print(c2.contactos)
print(p.contactos)
print(p2.contactos)
