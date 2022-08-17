from functools import reduce

def main():
    lista_numeros = list(map(int,set(input('Introduzca una lista de números separados por \",\" y sin espacios:').split(','))))
    resultado = reduce(lambda a,b: a+b,filter(lambda x: x % 2 != 0, lista_numeros))

    print('El resultado de sumar los números impares es: ',resultado)



if __name__ == '__main__':
    main()
