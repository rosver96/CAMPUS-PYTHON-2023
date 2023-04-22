print("\n\n")

estudiantes = int(input("ingresa la cantidad de estudiantes: "))
masculino = 0
femenino = 0
promedioEdad= 0
promedioNotas = 0
genero = ""
notaFinal = 0
suma = 0

for i in range(estudiantes):
    genero = input("ingresa tu genero (Masculino/Femenino): ")
    if genero == "masculino" or masculino == "MASCULINO":
        masculino += 1
    else:    
        femenino == "femenino" or femenino == "FEMENINO"
        femenino += 1

    edad = int(input("ingresa tu edad: "))
    n1 = int(input("ingresa la nota #1: "))
    n2 = int(input("ingresa la nota #2: "))
    n3 = int(input("ingresa la nota #3: "))
    suma = suma + edad
    promedioEdad = suma/estudiantes    
    promedioNotas = (n1+n2+n3)/3
    notaFinal = promedioNotas/estudiantes

print("el total de alumnos masculinos son: ",masculino)
print("el total de alumnos femeninos son: ",femenino)
print("el promedio de edades son: ",promedioEdad)
print("el promedio de notas son: ",promedioNotas)
print("el promedio de la facultad es: ",notaFinal)




