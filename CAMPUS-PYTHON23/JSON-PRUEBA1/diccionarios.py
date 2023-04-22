print("\n\n")
import os

dic_estudiantes = {
    1: { "nombre":     "juan jose",
         "apellido":   "diaz diaz",
         "correo":     " juanjo@gmail.com"},
    2: { "nombre":     "karen juliana",
         "apellido":   "orduz martinez",
         "correo":     " karen@gmail.com"},
    3: { "nombre":     "carlos jose",
         "apellido":   "ortiz manrique",
         "correo":     " kjose@gmail.com"},
    4: { "nombre":     "manuel jacinto",
         "apellido":   "gomez uriel",
         "correo":     " manuel1@gmail.com"},
    5: { "nombre":     "paola jimena",
         "apellido":   "duque tellez",
         "correo":     "jimenap2@gmail.com"},
}

dic_materias = {
    1 : {"nombre":"matematicas"},
    2 : {"nombre":"quimica"},
    3 : {"nombre":"ingles"},
    4 : {"nombre":"fisica"},
    5 : {"nombre":"ciencias politicas"},
}

# menu principal...............................................................................
def verMenu():
    os.system("clear")
    print(".............................. -.-COLEGIO-.- ...................................\n")
    print(""" seleccione alguna de las siguientes opciones:
    1). notas      2).estudiantes
    3).materias    0).salir """)
    
# materias.....................................................................................
def ver_Menu_materias(materias):
    os.system("clear")
    print(".............................. -.-MATERIAS-.- ..................................\n")
    print("CODIGO\t\t NOMBRE\n")
    for materia in materias:
        print(materia, "\t\t\t",materias[materia]["nombre"])
    print(""" seleccione alguna de las siguientes opciones:)
    1).crear       2).editar
    3).eliminar    0).salir """)

verMenu()
opcMenu = input()
while opcMenu != "0":
    if opcMenu == "1":
        print("..............................  -.-NOTAS-.- .......................................\n")
    elif opcMenu =="2":
        print("...............................  -.-ESTUDIANTES -.- ................................\n")
    elif opcMenu =="3":
        print("...............................  -.-MATERIAS -.- ...................................\n")
        ver_Menu_materias(dic_materias)
        opc = input()
    while opc != "0":
        if opc == "1":
            print("................................ -.- CREAR -.- ..............................\n")
            id = list(dic_materias.keys())[len(dic_materias)-1]+1
            print("por favor ingrese el nombre de la materia: ")
            dic_materias[id]["nombre"]=input()
        elif opc == "2":
            print("............................... -.- EDITAR -.- ..............................\n")
            print("por favor ingrese el codigo de la materia: ")
            id = int(input())
            print("por favor ingrese el nuevo nombre de la materia: ")
            dic_materias[id]["nombre"] = input()
        elif opc == "3":
            print("............................... -.- ELIMINAR -.- ..............................\n")
            print("por favor ingrese el codigo de la materia A eliminar: ")
            id = int(input())
            del (dic_materias[id])
        else:
                print("por favor ingrese una opcion valida\n")
                ver_Menu_materias(dic_materias)
                opc = input()
    else:
        print("por favor ingrese una opcion valida\n")
    verMenu
    opcMenu = input()
print("\n\n")
