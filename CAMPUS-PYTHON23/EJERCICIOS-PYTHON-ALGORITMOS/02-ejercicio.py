# 2.Crea una aplicación que nos pida un número por teclado y con una función se lo pasamos
# por parámetro para que nos indique si es o no un número primo, debe devolver true si
# es primo sino false.
# Un número primo es aquel solo puede dividirse entre 1 y si mismo.
# Por ejemplo: 25 no es primo, ya que 25 es divisible entre 5, sin embargo, 17 si es primo.


num1 = int(input(" ingrese un numero: "))

def primo(num):
    contador = 0
    for i in range(1,num+1):
        if num % i == 0:
            contador+=1

    if contador == 2:
        return True
    else:
        return False
        
esPrimo=primo(num1)
print(esPrimo)
            

