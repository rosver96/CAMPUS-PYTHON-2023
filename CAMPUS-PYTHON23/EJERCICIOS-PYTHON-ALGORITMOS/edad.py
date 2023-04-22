# Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.

print("\n\n")
edad = int(input("por favor ingrese su edad: "))
if edad >= 18:
    print("eres mayor de edad")
elif edad <18:
    print("eres menor de edad")
elif edad <= 0:
    print("ingresa una edad valida")