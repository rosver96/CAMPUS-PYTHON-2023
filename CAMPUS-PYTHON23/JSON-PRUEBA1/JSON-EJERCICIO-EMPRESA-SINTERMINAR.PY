print("\n\n")

import json 

dic_empresa = {
    
    "personas":[  
        {"id":1,
         "nombre":"pedro",
         "edad":24,
         "numero":3123654782},
    ]
}


def verMenu():
    print(" ******** MENU PERSONAS *******\n")
    print(" 1).crear nuevo paciente \n 2).editar datos paciente \n 3).borrar datos paciente \n 4).listar todos los pacientes \n 0).salir")


#fase apertura y actualizar 
def apertura(dic_empresa):
    with open("dic_empresa.json","w") as archivo:
        json.dump(dic_empresa,archivo)
        #fase de cierre
        archivo.close()


print("************************ DATOS EMPRESA ***************************************\n")

def crear (lista):
    id = len(lista)     # agregar al diccionario
    return id +1

def agregar(id):
    print("************************ AGREGAR ***************************************\n")
    print(input("ingrese un nombre: "))
    nombre=input()
    print(input("ingrese una edad: "))
    edad= input()
    print(int(input("ingrese un numero: ")))
    numero= int(input())
    
    dic_empresa["personas"].append({"id":id,"nombre": nombre,"edad": edad,"numero": numero})


def listar(persona):
    print("************************ LISTAR ***************************************\n")
    print("CODIGO"+"\t\t"+"NOMBRE"+"\t\t\t"+"EDAD"+"\t\t"+"NUMERO")
    with open("lista.json","r") as archivo:
        lista=json.load(archivo)
    #fase de cierre
    archivo.close()
    for i in persona:
        print(persona[i]["id"],"\t\t", persona[i]["nombre"],"\t\t", persona[i]["edad"],"\t\t", persona[i]["numero"],"\n")
    listar()

verMenu()

opc = int(input())
while opc != 0:
    if opc == 1:
        id = crear(dic_empresa)
        agregar(id)
        apertura(dic_empresa)
        print("************ AGREGADO EXITOSAMENTE ************\n")
