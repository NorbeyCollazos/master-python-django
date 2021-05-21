#condicionales

"""
OPERADORES DE COMPARACIÓN
==  igual
!=  diferente
<   menor igual que
>   mayor igual que
<=  menor igual
>=  mayor igual

"""

#ejemplo 1

print("****************ejemplo 1******")

color = "Azul"
if color == "azul":
    print("Es correcto")
else:
    print("No adivinaste")


    #if anidados

print("****************ejemplo if anidados******")

nombre = "Norbey"
ciudad = "Garzón"
continente = "LatinoAmerica"
edad = 27
mayoria_edad = 18

if edad >= mayoria_edad:
    print(f"{nombre} es mayor de edad")

    if continente != "LatinoAmerica":
        print("No es Latino")
    else:
        print(f"{nombre} es latino")


else:
    print(nombre + " no es mayor de edad")