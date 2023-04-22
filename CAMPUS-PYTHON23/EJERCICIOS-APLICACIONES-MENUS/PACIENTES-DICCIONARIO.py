rint("\n\n")

import os
import time
import json
opcMenu = ""
otro = 1
dicPacientes = {}

# FUNCIONES DE LOS PACIENTES----------------------------------------------------------------------------------------------------
def verMenu():
    os.system("cls")
    print("**************** PACIENTES ****************")
    print("Seleccione alguna de las siguientes opciones:\n0.Salir\n1.Agregar\n2.Editar\n3.Eliminar\n4.Listar pacientes")


def crearId(diccionario):
    id = len(diccionario)
    return (id + 1) 

def agregarPaciente(pacientes, nombrePaciente, edadPaciente, pesoPaciente, sexoPaciente):
    id = crearId(pacientes)
    pacientes[id] = {
        "nombre": nombrePaciente,
        "edad": edadPaciente,
        "peso": pesoPaciente,
        "sexo": sexoPaciente
    }
    return pacientes

def verPacientes(pacientes):
    listaPacientes = "CODIGO\t\tNOMBRE\t\t\t\tEDAD\t\tPESO\t\tSEXO\n"
    for paciente in pacientes:
        listaPacientes += str(paciente) + "\t\t" + pacientes[paciente]["nombre"] + "\t\t" + str(pacientes[paciente]["edad"]) + "\t\t" + str(pacientes[paciente]["peso"]) + "\t\t" + pacientes[paciente]["sexo"] + "\n"
    return listaPacientes


verMenu()
opcMenu = input("\nSelecciona la opcion deseada: ")
otro = 1
m = len(dicPacientes)
while otro != 0:
    if opcMenu == "1":
        print("\n******************************* AGREGAR *******************************")
        nomPaciente = input("Ingrese el nombre del paciente a agregar: ")
        edad = int(input("Ingrese la edad del paciente a agregar: "))
        peso = float(input("Ingrese el peso del paciente a agregar: "))
        sexo = input("Ingrese el sexo del paciente a agregar: ")
        dicEstudiantes = agregarPaciente(dicPacientes, nomPaciente, edad, peso, sexo)
        print("************ PACIENTE AGREGADO EXITOSAMENTE ************")
        time.sleep(3)
    elif opcMenu == "2":
        print("\n******************************* EDITAR *******************************")
        codigo = int(input("Ingrese el codigo del estudiante a editar: "))
        dicPacientes[codigo]["nomPaciente"] = input("Ingrese el nombre del nuevo paciente: ")
        dicPacientes[codigo]["edad"] = int(input("Ingrese la edad del nuevo paciente: "))
        dicPacientes[codigo]["peso"] = float(input("Ingrese el peso del nuevo paciente: "))
        dicPacientes[codigo]["sexo"] = input("Ingrese el sexo del nuevo paciente: ")
        print("************ PACIENTE ACTUALIZADO EXITOSAMENTE ************")
        time.sleep(3)
    elif opcMenu == "3":
        print("\n******************************* ELIMINAR *******************************")
        codigo = int(input("Ingrese el codigo del paciente a eliminar: "))
        del(dicEstudiantes[codigo])
        print("************ PACIENTE ELIMINADO EXITOSAMENTE ************")
        time.sleep(3)
    elif opcMenu == "4":
        print(verPacientes(dicPacientes))
    else:
        print("Por favor ingrese una opcion valida")
        time.sleep(3)
    otro = int(input("0.Salir\n1.Otro\n):_"))
    verMenu()
    opcMenu = input("Selecciona la opcion deseada: ")

print("\n\n")
