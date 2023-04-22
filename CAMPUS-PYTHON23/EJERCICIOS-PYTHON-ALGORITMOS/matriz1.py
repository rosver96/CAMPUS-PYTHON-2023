op = True

nombre=[]
nota1=[]
nota2=[]
nota3=[]
promedio =[]

while op:

    menu = input("\ningresar la opcion\n1.agregar estudiante y sus notas \n2).salir del programa e imprimir la lista \n")

    if menu =="1":
        nombre1 = input(" ingrese su nombre: ")
        nombre.append(nombre1)
        nota1_1 = float(input(" ingrese la nota #1 del estudiante: "))
        nota1.append(nota1_1)
        nota2_2 = float(input(" ingrese la nota #2 del estudiante: "))
        nota2.append(nota2_2)
        nota3_3 = float(input(" ingrese la nota #3 del estudiante: "))
        nota3.append(nota3_3)
        promedio.append((nota1_1 + nota2_2 + nota3_3)/3)
        matriz = [nombre,nota1,nota2,nota3,promedio]

    else:
        print("estudiante" + "\t" + "n1" + "\t""\t" +  "n2" + "\t""\t" +  "n3" + "\t"  +  "\t""\t""nf")
        for i in range (len(nota1)):
            for j in range(5):
                print(matriz[j][i], end= 2* "\t")
            print("\n")
        op == False




