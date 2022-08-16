
class Alumno():
    _nombre: str
    _nota: float

    def __init__(self, nombre: str = "Pedro", nota: int = 10):
        self._nombre = nombre
        self._nota = nota

    def setNombre(self, nombre):
        self._nombre = nombre

    def setNota(self, nota):
        self._nota = nota

    def getNombre(self):
        return self._nombre

    def getNota(self):
        return self._nota


    def showAlumno(self):
        print("Alumno: ", self.getNombre(), "\nNota: ", self.getNota(), "\n")
        if(self._nota <5):
            print("Resultado: Suspenso\n")
        else:
            print("Resultado: Aprobado\n")

juan = Alumno("Juan", 7.5)
marta = Alumno("Marta", 4.5)

juan.showAlumno()
marta.showAlumno()