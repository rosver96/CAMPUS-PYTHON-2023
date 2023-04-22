print("\n\n")
import os

basico = {
    "trainer" : "",
    1:{"nombre": "",
       "mes de ingreso": "",
       "grupo" : "",
       "edad": ""
       }
}
intermedio = {
    "trainer" : "",
    1: { "nombre" : "",
         "mes ingreso" : "",
         "grupo" : "",
         "edad" : ""
    }
}
avanzado = {
    "trainer" : "",
    1: { "nombre" : "",
         "mes ingreso" : "",
         "grupo" : "",
         "edad" : ""
    }
}
#menu principal.......................................................................
def verMenu():
    os.system("clear")
    print("-------------  MANTENIMIENTO Y PREMIOS CAMPERS CAMPUS  ------------------")
    print("-------------------------------------------------------------------------")

    print(" 0. TERMINAR PROCESO")
    print("-------------------------------------------------------------------------")
    print(" 1. CREAR GRUPO BASICO CON CAMPERS Y SUS DATOS PERSONALES")
    print(" 2. REGISTRAR EXPERT TRAINER DEL GRUPO BASICO")
    print(" 3. LISTAR CAMPERS")
    print(" 4. REPORTAR CAMPERS DE MENOR Y MAYOR EDAD") 
    print("ingrese una opcion: --")
    
def crearPrimerEstudiante ():
    print("........................ CREAR ESTUDIANTE  ............................\n")
    print("por favor ingrese el nombre del camper: ")
    basico[1]["nombre"]=input()
    print("por favor ingrese mes de ingreso: ")
    basico[1]["mes de ingreso"]=input()
    print("por favor ingrese el grupo: ")
    basico[1]["grupo"]=input()
    print("por favor ingrese su edad: ")
    basico[1]["edad"]=int(input())
    
def crearTrainer ():
    print(".......................... CREAR TRAINER  ...........................\n")
    print("por favor ingrese el nombre del trainer: ")
    basico["trainer"]=input()
    
def listarCampers():
    print("....................... LISTAR CAMPERS  .............................\n")
    
    
def reportarCampersEdades():
    print(".............. REPORTAR CAMPERS DE MENOR Y MAYOR EDAD  ..............\n")
    

verMenu()
opcMenu = input()

while opcMenu != "0":
    if opcMenu == "1":
        crearPrimerEstudiante()
    elif opcMenu == "2":
        crearTrainer()
    elif opcMenu == "3":
        listarCampers()
    elif opcMenu == 4:
        reportarCampersEdades()
    else:
        print("Por favor ingrese una opcion valida")
        
    verMenu()     
    opcMenu= input()  
      
