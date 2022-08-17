def main():
    lista_paises = []

    lista_paises = input('Introduzca una lista de países separados por \",\" y sin espacios:').split(',')
    lista_paises = set(lista_paises)
    lista_paises = sorted(list(lista_paises))

    resultado_lista = ''
    for x in lista_paises:
        if lista_paises.index(x) == 0:
            resultado_lista += x
        else:
            resultado_lista += ', ' + x

    print(f'La lista resultante es:\n{resultado_lista}')


if __name__ == '__main__':
    main()
