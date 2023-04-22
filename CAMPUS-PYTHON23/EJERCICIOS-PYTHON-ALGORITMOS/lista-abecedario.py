print("\n\n")

a = 0
e = 0
y = 0
o = 0
u = 0


mi_lista = []

letra1 = int(input("ingrese la cantidad de letras: "))

for i in range (letra1):
    letra = input("ingrese una letra: ")
    mi_lista.append(letra)

for letra in mi_lista:
    if letra == "a":
        a +=1
    elif letra == "e":
        e +=1
    elif letra == "i":
        y +=1
    elif letra == "o":
        o +=1
    elif letra == "u":
        u +=1   
        
print("la cantidad de a es: ",a)
print("la cantidad de e es: ",e)
print("la cantidad de i es: ",y)
print("la cantidad de o es: ",o)
print("la cantidad de u es: ",u)


