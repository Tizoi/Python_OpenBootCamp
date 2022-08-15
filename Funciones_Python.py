temperatura = 25


def nombre(nombre):
    global temperatura
    temperatura = 20
    print("Hola, ", nombre, "hoy hace ", temperatura, " grados")

def matematicas(a, b):
    def suma(a, b, c = 5):
        print(a + b + c)

    def resta(*args):
        print(args[0])
        print(a - b)
    def multiplicacion(**kwargs):
        for key, value in kwargs.items():
            print(key, "=", value)
        if 'coche' in kwargs and kwargs["coche"] == 'bonito':
            print("Tu coche es bonito")

    suma(a,b)
    resta(a,b)
    multiplicacion(vivienda = "piso", coche = "bonito")

def operaciones (a, b):
    return a+b, a-b, a/b, a*b

anonima = lambda nombre: print("hola, ", nombre)


matematicas(1 , 2)

nombre("Abel")

suma, resta, division, multiplicacion = operaciones(2,2)

resultados = operaciones(3,3)

anonima("pepe")


