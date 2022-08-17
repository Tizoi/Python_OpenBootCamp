import _thread
import time
import logging
from functools import reduce

def miFuncion(x) -> bool:
    if x % 2 == 0:
        return True

    return False

def cuadrado(x):
    return x*x

def suma(a, b):
    print(f'a = {a} b = {b}')
    return a+b


def horaActual(nombre_thread, tiempo_de_espera):
    count = 0

    while count<5:
        time.sleep(tiempo_de_espera)
        count += 1
        print(f'hilo: {nombre_thread} - {time.ctime(time.time())}')

_thread.start_new_thread(horaActual, ('thread 1', 1))

_thread.start_new_thread(horaActual, ('thread 2', 2))

logging.basicConfig(level = logging.DEBUG)
logging.debug('buggazo')
logging.info("Arrancando programa")
logging.warning('HACE CALOR')
logging.error('test')
logging.critical('lolazo')

numero = [1 ,2 ,3 ,4 ,5 ,6 ,7 ,8 ,9 ,10]

resultado = filter(miFuncion, numero)
print(list(resultado))

resultado = filter(lambda x: x % 2 == 0, numero)
print(list(resultado))

resultado = map(cuadrado, numero)
print(list(resultado))

resultado = reduce(suma, numero)

print(resultado)

cursos = ['Java', 'Python', 'Git']
asistentes = [15, 20, 4]
demo = zip(cursos, asistentes)
print(list(demo))

listaA = [1 == 1, 2 == 2, 3 == 4]
res = any(listaA)
print(res)
res = all(listaA)
print(res)

a = 5.5
b = 5.4
c = 5.6

print(round(a))
print(round(b))
print(round(c))

print(min(2,3,4,5,6,7,8,9))

lista = ['z', 'c', 'a','y','b']
ordenada = sorted(lista)
print(ordenada)

# from getpass import getpass



i = 0
while i<50:
    time.sleep(0.2)
    i+=1
