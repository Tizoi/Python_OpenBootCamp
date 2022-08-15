class Juguete:
    encendido = False #Para indicar que un atributo es privado se guioniza: _encendido

    def enciende(self):
        self.encendido = True
class Estatica:
    numero = 1

    def incrementa ():
        Estatica.numero += 1

class Dino(Juguete):
    escamas = True

    def __init__(self):
        pass
    def __del__(self):
        pass




dino = Juguete()
dino.enciende()
print(dino.encendido)
dino.encendido = False
print(dino.encendido)

dino2 = Dino()

print(dino2.escamas)
print(dino2.encendido)

print(Estatica.numero)
Estatica.incrementa()
print(Estatica.numero)


