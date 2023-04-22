#3.Escribir un programa para solicitar al usuario el ingreso de un número entero y que luego imprima un valor de verdad 
# dependiendo de si el número es par o no. Recordar que un número es par si el resto, al dividirlo por 2, es 0.


print("\n\n") 


numero =int(input("ingrese un numero entero : "))
if numero % 2 ==0:
    print(" el numero es par : ")
else:
    print(" el numero es impar")


print("\n\n") 