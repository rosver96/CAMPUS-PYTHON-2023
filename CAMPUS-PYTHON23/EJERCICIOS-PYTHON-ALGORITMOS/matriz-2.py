estudiantes = []
num_estudiantes = int(input("ingrese la cantidad de estudiantes: "))
impresion = []

for i in range(num_estudiantes):
    nombre = input("ingrese el nombre del estudiante: ")
    n1 = float(input("ingrese la primera nota del estudiante: "))
    n2 = float(input("ingrese la segunda nota del estudiante: "))
    n3 = float(input("ingrese la tercera nota del estudiante: "))
    prom = (n1+n2+n2)/3
    estudiantes.append([nombre,n1,n2,n3,prom])
    
print("\nNombre\t\tn1\t\tn2\t\tn3\t\tnf")
impresion = ""
for estudiante in estudiantes:
    for i in range(5):
        impresion+= str(estudiante[i])+ "\t\t"
    impresion += "\n"  
print(impresion)
print("\n\n")