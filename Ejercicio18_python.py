from pickle import *


class Vehiculo():
    _motor: str
    _puertas: int
    _ventanas: int

    def __init__(self, motor = '', puertas = 0, ventanas = 0):
        self._motor = motor
        self._puertas = puertas
        self._ventanas = ventanas

    def setMotor(self, motor: str):
        self._motor = motor

    def getMotor(self) -> str:
        return self._motor

    def setPuertas(self, puertas: int):
        self._puertas = puertas

    def getPuertas(self) -> int:
        return self._puertas

    def setVentanas(self, ventanas: int):
        self._ventanas = ventanas

    def getVentanas(self) -> int:
        return self._ventanas

    def __repr__(self) -> str:
        return f'{self.__class__} con motor: {self._motor}, {self._puertas} puertas y {self._ventanas} ventanas en {hex(id(self))}'








def main():

    miCoche = Vehiculo('125cc Diesel', 4, 4)

    print(miCoche)

    f = open('miFicheroBinario', 'w+b')
    dump(miCoche, f)
    f.close()

    f = open('miFicheroBinario', 'rb')
    f.seek(0)
    print('Nuestro archivo binario:')
    print(f.read())


    f.seek(0)

    nuevoCoche = load(f)
    print('Clase del objeto guardado en fichero: ',type(nuevoCoche))
    print('Printout del objeto guardado: ', nuevoCoche)

    f.close()




if __name__ == '__main__':
    main()