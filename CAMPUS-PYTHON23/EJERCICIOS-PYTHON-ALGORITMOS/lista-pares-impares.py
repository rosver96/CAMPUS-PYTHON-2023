
lista=[]
numero=int(input("Ingrese numero entero: "))
#la variable suma sera la que guardara la cantidad 
#de numeros pares
suma=0
        
while numero!=99999:
    lista.append(numero)
    if numero%2==0:
        suma=suma+1
    numero=int(input("Ingrese numero entero: "))

impares=len(lista)-suma
print("El numero de numeros pares es: ",suma)
print("El numero de numeros impares es: ",impares)
        