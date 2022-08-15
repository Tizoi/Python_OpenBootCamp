def is_Bisiesto(year: int) -> str:
    if (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)):
        return "Es bisiesto "
    else:
        return "No es bisiesto"


print(f"El año 2000 " + str(is_Bisiesto(2000)))
print(f"El año 1900 " + str(is_Bisiesto(1900)))

year = int(input("Introduzca un año para comprobar si es bisiesto: "))

print(is_Bisiesto(year))
