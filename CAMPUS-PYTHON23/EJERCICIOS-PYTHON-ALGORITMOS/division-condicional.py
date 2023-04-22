# Escribir un programa que pida al usuario dos números y muestre por pantalla su división. 
# Si el divisor es cero el programa debe mostrar un error.

print("\n\n")
# def division(a,b):
#     return a / b

numero1 = float(input("ingrese un numero: "))
numero2 = float(input("ingrese el segundo numero: "))

# print(division(numero1, numero2))

if numero2 == 0:
    print("ingrese un valor valido el cual dividir")
else:
    print(numero1/numero2)



# opcion mejorada _________________________________________________________________________________
n = float(input("Introduce el dividendo: "))
m = float(input("Introduce el divisior: "))
if m == 0:
    print("¡Error! No se puede dividir por 0.")
else:
    print(n/m)