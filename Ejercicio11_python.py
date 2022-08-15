def is_Primo(numero: int) -> str:
    if(numero%2 == 0):
        return "No es primo"
    else:
        return "Es primo"

print(is_Primo(5))
print(is_Primo(6))

numero = int(input("Introduzca un número entero para comprobar si es o no primo:"))

print(is_Primo(numero))
