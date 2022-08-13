

a = 4
b = 6

if a >= 5 and b <= 6:
    print("A es mayor o igual que 5 y B es menor o igual que 6")
elif a >= 6:
    print("A es mayor o igual que 6")
else:
    print("No se cumple NADA de lo anterior")

x = 0

while x < 10:
    print("contador X vale: ", x)
    x += 1

    if x % 2 == 0:
        print(x, "es par.")
        continue # puede crear bucle infinito si no se ha actualizado el contador porque vuelve a la condición

    if x == 5:
        break

lista = [1,2,3,4,5,6,7,8,9,10]

for valorActual in lista:
    print(valorActual)

#[1,10)
for valorActual in range(1,10):
    print(valorActual)

lista  = [1,2,3,4,'a']
longitud = len(lista)

for contador in range(longitud):
    print(lista[contador])

lista = ["hola","mensaje","adios"]

for palabra in lista:
    print("Palabra actual:", palabra)
if "mensaje" in lista:
    print("He encontrado la palabra mensaje")

lista.pop('mensaje')

for palabra in lista:
    if palabra == 'mensaje':
        print("He encontrado la palabra mensaje")
        break
else:
    print("no encuentro nada")
#pass


# Switches
#version anterior a python 3.10
valor = 5
if valor == 1:
    print("Valor es igual 1")
elif valor == 2:
    print("Valor es igual 2")
elif valor == 3:
    print("Valor es igual 3")
elif valor == 4:
    print("Valor es igual 4")
elif valor == 5:
    print("Valor es igual 5")
# nueva versión
match valor:
    case 1:
        print("Valor es igual 1")
    case 2:
        print("Valor es igual 2")
    case 3:
        print("Valor es igual 3")
    case 4:
        print("Valor es igual 4")
    case 5:
        print("Valor es igual 5")