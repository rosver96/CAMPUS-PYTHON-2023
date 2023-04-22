# hacer una calculadora con funciones en python
print("\n\n")
def suma (a,b):
    return a + b

def resta ( a,b):
    return a - b
def multiplicacion (a,b):
    return a * b
def division (a,b):
    return a / b
def divisionEntera(a,b):
    return a // b
def exponenciasion(a,b):
    return a ** b

def raiz (a,b):
    return a ** (1/b)
print("---------- CALCULADORA SIMPLE--------------")
print(" 1).suma \n 2).resta \n 3).multiplicacion \n 4).division \n 5).D.entera \n 6).exponenciasion \n 7).raiz")
opc = int(input("ingresa el numero de la operacion deseada: -"))
numero1 = float(input("por favor ingresa un numero: "))
numero2 = float(input("por favor ingresa un numero: "))

if opc == 1:
    print("RESULTADO: ",suma(numero1, numero2))
elif opc == 2:
    print("RESULTADO: ",resta(numero1,numero2))
elif opc == 3:
    print("RESULTADO: ",multiplicacion(numero1,numero2))
elif opc == 4:
    print("RESULTADO: ",division(numero1,numero2))
elif opc == 5:
    print("RESULTADO: ",divisionEntera(numero1,numero2))
elif opc == 6:
    print("RESULTADO: ",exponenciasion(numero1,numero2))
elif opc == 7:
    print("RESULTADO: ",raiz(numero1,numero2))
else:
    print("ingrese una opcion valida")