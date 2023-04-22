"""Se desea realizar un programa en el cual se ingresen números enteros, los cuales
se deben almacenar en una lista. Se debe ingresar números hasta que el número
ingresado sea 99999. Una vez creada la lista, se desea conocer cuales y cuántos
son pares e impares."""

lista = []
suma= 0

numero = int(input("ingrese un numero entero: "))

while numero != 99999:
    lista.append(numero)
    if numero % 2 == 0:
        suma = suma+1
    numero = int(input(" ingrese un numero entero: "))

impares = len(lista)-suma

print("los numeros que ingreso son: ",lista)
print("el total de numeros pares son: ",suma)
print("el total de numero impares son: ",impares)
    
