print("\n\n")

suma=0
numero = int(input("ingrese un numero entero: "))

while numero != 0:
    numero = int(input("ingrese un numero entero: "))
    suma = suma + numero
    if numero == 0:
        print("el programa ha finalizado")

print("la sumatoria de los numero es: ",suma)