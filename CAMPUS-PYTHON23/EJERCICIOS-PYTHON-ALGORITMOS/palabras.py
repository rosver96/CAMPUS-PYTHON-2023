"""Dada una lista con nombres completos de personas, realizar un programa que
genere una segunda con la cantidad de palabras de cada uno de los nombres. La
lista de nombres debe llenarse a través de nombres que se ingresan por teclado,
hasta que el nombre ingresado sea “FIN”
Se debe imprimir la lista de nombres y la lista con la cantidad de palabras de cada
nombre."""


lista = []
cantidad= []
nombre = input("ingrese un nombre: ")

while nombre != "fin" :
    lista.append(nombre)
    x = len(nombre.split(" "))

    cantidad.append(x)
    nombre = input("ingrese el nombre completo: ")


print("la lista generada es: ",lista)
print("la lista con cantidad de palabras es: ",cantidad)

print("..........................")
for i in range (len(lista)):
    print("para el nombre: ",lista[i], "la cantidad de palabras es: ",cantidad[i])


