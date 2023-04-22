print("\n\n")

def factorial(n):
    f = 1
    for i in range(1,n +1):
        f = f*i
    return f
 
n = int(input("ingresa el numero n: "))
r = int(input("ingresa el numero r: "))    #no puede ser mayor que n

c = factorial(n)/(factorial(n-r)* factorial(r))

print("el resultado es: ",c)