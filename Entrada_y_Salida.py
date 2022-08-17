
numero = 34
texto = "quijote"
decimal = 1.2

#formateo de texto: forma antigua
print("El numero es %d y el texto es %s y tiene %.2f" % (numero, texto, decimal))

#formato Python 2.6 hasta 3.6, funcion format
print("El numero es {} y el texto es {} y tiene {}".format(numero, texto, decimal))

#fstrings
print(f'El numero es {numero} y el texto es {texto} y tiene {decimal}')
