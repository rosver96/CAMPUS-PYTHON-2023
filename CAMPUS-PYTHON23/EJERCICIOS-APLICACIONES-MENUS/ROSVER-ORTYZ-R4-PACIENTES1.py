print("\n\n")

dic_paciente = {}


# funcion menu
def verMenu():
    print(" ******** MENU PACIENTES *******\n")
    print(" 1).crear nuevo paciente \n 2).editar datos paciente \n 3).borrar datos paciente \n 4).listar todos los pacientes \n 0).salir")
    
# funcion crear   
def crear (dic):
    id = len(dic)  # agregar al diccionario
    return id +1

#funcion agregar
def agregar(id):
    nombre = input("ingrese el nombre: ")
    fechaNac = input("ingresa la fecha de nacimiento: ")
    peso = float(input("ingrese el peso: "))
    sexo = input("ingrese un sexo (Hombre/mujer): ")
    
    dic_paciente[id] = {"nombre": nombre,"fechaNac": fechaNac,"peso": peso,"sexo": sexo}

#funcion listar
def verPacientes(pacientes):
    print("CODIGO"+"\t\t"+"NOMBRE"+"\t\t\t"+"FECHANAC"+"\t\t"+"PESO"+"\t\t"+"SEXO")
    for i in pacientes:
        print(i,"\t\t", pacientes[i]["nombre"],"\t\t", pacientes[i]["fechaNac"],"\t\t", pacientes[i]["peso"],"\t\t",pacientes[i]["sexo"],"\n")

verMenu()


opc = int(input())
while opc != 0:
    if opc == 1:
        print("******** CREAR **********")
        id = crear(dic_paciente)
        agregar(id)
        print("************ AGREGADO EXITOSAMENTE ************\n")
    elif opc == 2:
        print("******** EDITAR *********\n")
        print("Por favor ingrese el código del paciente que desea editar: ")
        id = int(input())
        print("Que quiere editar: ")
        print("1).Nombre \n2).fecha de nacimiento \n3).peso \n4).sexo ")            
                      
        update = int(input())
        if update == 1:
                print("Por favor ingrese el nuevo nombre del paciente: ")
                dic_paciente[id]["nombre"] = input()
                print(dic_paciente)
        elif update == 2:
                print("Por favor ingrese la nueva fecha de nacimiento: ")
                dic_paciente[id]["fecha de nacimiento"] = input()
        elif update == 3:
                print("Por favor ingrese el nuevo peso del paciente: ")
                dic_paciente[id]["peso"] = input() 
        elif update == 4:
                print("Por favor ingrese el sexo del paciente: ")
                dic_paciente[id]["sexo"] = input() 
                print("************ ACTUALIZADO EXITOSAMENTE ************\n")
    elif opc == 3:
        print("******** BORRAR *********\n")
        id = int(input("ingrese el id del paciente a eliminar: "))
        del dic_paciente[id]
        print("************ ELIMINADO EXITOSAMENTE ************\n")
    elif opc == 4:
        print("******** LISTAR *********\n")
        print(verPacientes(dic_paciente))
    else:
        print("ingrese una opcion valida: ")
        
    verMenu()
    opc = int(input())
