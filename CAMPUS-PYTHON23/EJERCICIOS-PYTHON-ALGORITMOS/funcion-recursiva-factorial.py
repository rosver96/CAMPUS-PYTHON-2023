print("\n\n")

def factorial (n):
    if n == 0:
        return(1)
    else:
        return (n *factorial(n-1))
    
n = int(input("ingresa el numero n: "))
r = int(input("ingresa el numero r: ")) 
c = factorial(n)/(factorial(n-r)* factorial(r))

print("el resultado es: ",c)