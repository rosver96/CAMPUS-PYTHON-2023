lista=[]
cantidad=[]
nombre=input("Ingresa nombre: ")

while nombre!="FIN":
    lista.append(nombre)
    #la parte nombre.split(" ") es para crear una lista con elementos 
    #los cuales estan en el string separados con espacio " " 
    #cantidad de palabras del nombre completo
    x=len(nombre.split(" "))
    #se agrega a otra lista la cantidad de palabras
    cantidad.append(x)
    nombre=input("Ingresa nombre completo: ")

print("La lista generada fue: ",lista)
print("Lista con cantidad de palbras es: ",cantidad)

#Imprime junto a cada nombre la cantidad de palabras que tiene el nombre
print("------------")
for i in range(len(lista)):
    print("Para el nombre ",lista[i], " la cantidad de palabras es: ",cantidad[i])
        