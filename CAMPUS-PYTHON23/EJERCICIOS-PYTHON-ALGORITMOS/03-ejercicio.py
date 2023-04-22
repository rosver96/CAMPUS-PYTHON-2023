#3.Crea una aplicación que nos calcule el factorial de un número pedido por teclado, lo
# realizara mediante una función al que le pasamos el número como parámetro. Para calcular el
# multiplica los números anteriores hasta llegar a uno. Por ejemplo, si introducimos un 5,
# realizara esta operación 5*4*3*2*1=120.


def factorial (numero):
    if (numero==0):
        return 1
    else:
        return numero * factorial(numero-1)
numero = int(input("ingrese un numero: "))    
print("el factorial es : ",factorial(numero))
# print("el factorial de: " + str(numero) + ": es : " + str(factorial(numero)))



