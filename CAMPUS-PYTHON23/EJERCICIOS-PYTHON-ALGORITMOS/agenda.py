rta = True
estudiante = []
while rta == True:
    print("1).registro de estudiante\n2).registro de quices\n3).registro de trabajos\n4).registro de parciales\nEnter para salir")
    rta=input(":)_")
    if rta == "1":
       nombre = input("ingrese nombre : ")
       codigo = input("ingrese codigo : ")
       estudiante.append([nombre,codigo,[],[],[]])
    elif rta == "2":
        palabra = input ("ingrese codigo del estudiante : ")
        for item in estudiante:
            if estudiante in item:
               notaq = float(input("ingrese nota del quiz : "))  
               print(estudiante)

rta = bool(input("desea ingresar otro estudiante (si) presione S de lo contrario presione Enter"))
print(estudiante)

       


       
       