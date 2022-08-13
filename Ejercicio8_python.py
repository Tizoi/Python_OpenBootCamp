# Este programa recibe dos números por consola e itera por el rango que conforman
# devolviendo una lista con los números impares del rango

inicio = int(input("Introduzca el número de inicio: "))
final = int(input("Introduzca el número final: "))

contador=inicio
numerosImpares=[]

while contador<= final:
    if(contador%2 != 0):
        numerosImpares.append(contador)
    contador+=1
print("La lista de números impares es: ",numerosImpares)
