# Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.
print("\n\n")
numero = int(input("ingrese un numero entero: "))

if numero % 2 == 0:
    print("El número " + str(numero) + " es par")
else:
    print("El número " + str(numero) + " es impar")