import os 
import time
import json

with open("estudiante.json", "r") as estudiante: dicEstudiante = json.load(estudiante)
with open("notas.json", "r") as notas: notas = json.load(notas)
with open("materias.json", "r") as materias: dicMaterias = json.load(materias)
count = 1
if len(notas) == 0:
    for i in dicMaterias:
        for j in dicEstudiante:
            notas[count] = {"estudiante": j, "materia": i, "nota1": "p", "nota2": "p", "nota3": "p", "notaf": "p"}
            count+=1
        with open("notas.json", "w") as archivo: json.dump(notas, archivo)
        
        
#------------------------MENUGENERADOR
def limpiarpantalla():
    os.system("clear")
    print("=================================== CAMPUS =================================")
    print('''Seleccione alguna de las siguientes opciones:
            1. Notas
            2. Estudiantes
            3. Materias
            0. Salir
            ''')
#----------------------MATERIAS
def menumaterias(materias):
    os.system("clear")
    print(verMaterias(materias))
    print('''seleccione las siguientes opciones
            1. AGREGAR              2. ELIMNAR
            3. EDTIAR               ''')
def crearId(diccioneario):
    id = int(list(diccioneario.keys())[len(diccioneario) - 1 ]) if len(diccioneario) > 0 else 0
    return id + 1
def agregarMateria(materias, NombreMateria):
    id = crearId(materias)
    materias[id] = {
        "nomMateria": NombreMateria
    }
    return materias
def verMaterias(materias):
    os.system("clear")
    listamaterias = "CODIGO\t\tMATERIAS\n"
    for materia in materias:
        listamaterias +=  str(materia) + "\t\t" + materias[materia]["nomMateria"] + "\n"
    return listamaterias
#--------------------ESTUDIANTES
def showByEst(id,dicnotas):
    nota = "CODIGO\t\tESTUDIANTE\t\tMATERIA\t\tNOTA 1\t\tNOTA 2\t\tNOTA 3\t\tNOTA FINAL\n"
    for x in dicnotas:
        if dicnotas[x]["estudiante"] == id:
            nota +=  str(x) +  "\t\t" + str(dicEstudiante[dicnotas[x]["estudiante"]]["nombres"]) +"\t\t" + str(dicMaterias[dicnotas[x]["materia"]]["nomMateria"])  +"\t\t" + str(dicnotas[x]["nota1"]) + "\t\t" + str(dicnotas[x]["nota2"]) + "\t\t" + str(dicnotas[x]["nota3"]) +  "\t\t" + str(dicnotas[x]["notaf"]) + "\n"
    return nota
def agregarEstudiante(estudiante, nombre, apellido, correo):
    id = crearId(estudiante)
    estudiante[id] = {
        "nombres": nombre,
        "apellidos": apellido,
        "correo": correo,
    }
    return estudiante
def menuestudiantes(estudiantes):
    os.system("clear")
    print(verEstudiantes(estudiantes))
    print('''seleccione las siguientes opcionesr
            1. AGREGAR              2. EDITAR
            3. ELIMINAR             0. SALIR''')

def verEstudiantes(estudiantes):
    estudiante = "CODIGO\t\t\tNOMBRES\t\t\tAPELLIDOS\t\t\tCORREO\n"
    for x in estudiantes:
        estudiante +=  str(x) + "\t\t\t" + estudiantes[x]["nombres"] + "\t\t\t" + estudiantes[x]["apellidos"] + "\t\t\t" + estudiantes[x]["correo"] + "\n"
    return estudiante
opcMenu = "12"
#----------------------NOTAS
def editNotes(cod, nota, ch):
    if ch == "1":
        notas[cod]["nota1"] = nota
    elif ch == "2":
        notas[cod]["nota2"] = nota
    elif ch == "3":
        notas[cod]["nota3"] = nota
    notas[cod]["notaf"] =  round(sum(x for x in [notas[cod]["nota1"], notas[cod]["nota2"], notas[cod]["nota3"]]) / 3)
def agregarNotas(notas,asd, matId):
    id = crearId(notas)
    notas[id] = {
        "estudiante":asd,
        "materia":matId,
        "nota1": "p",
        "nota2": "p",
        "nota3": "p",
        "notaf": "p",
    }
    return notas
def vernotas(notar):
    nota = "CODIGO\t\tESTUDIANTE\t\tMATERIA\t\tNOTA 1\t\tNOTA 2\t\tNOTA 3\t\tNOTA FINAL\n"
    for x in notar:
        nota +=  str(x) +  "\t\t" + str(dicEstudiante[str(notar[x]["estudiante"])]["nombres"] ) +"\t\t" + str(dicMaterias[str(notar[x]["materia"])]["nomMateria"])  +"\t\t" + str(notar[x]["nota1"]) + "\t\t" + str(notar[x]["nota2"]) + "\t\t" + str(notar[x]["nota3"]) +  "\t\t" + str(notar[x]["notaf"]) + "\n"
    return nota
def menuNotas(notas):
    os.system("clear")
    print(vernotas(notas))
    print('''seleccione las siguientes opciones
            1. AGREGAR              2. EDITAR
            3. ELIMINAR             4. SUBIR NOTAS 
            5. VER POR ESTUDIANTE''')
#----------------------MENU
while opcMenu != "0":
    limpiarpantalla()
    opcMenu = input()
    if opcMenu == "1":
        print(menuNotas(notas))
        opc = input()
        while opc != "0":
            if opc == "1":
                print("==================== AGREGAR =================")
                print(verEstudiantes(dicEstudiante))
                print("ingrese el codigo del estudiante")
                estudianteid = int(input())
                print(verMaterias(dicMaterias))
                print("ingrese el codigo de la materia")
                materiaid = int(input())
                with open("notas.json", "w") as archivo: json.dump(agregarNotas(notas, estudianteid, materiaid), archivo)
                print("**************** MATERIA EDITADA EXITOSAMENTE ******************")
            if opc == "2":
                print(vernotas(notas))
                print("ingrese el codigo de la nota")
                notaest = int(input())
                print("ingrese la nota que desea editar \n1.Nota 1 \n2.Nota 2 \n3.Nota 3\n")
                notaop = input()
                print("ingrese la nota")
                nota = int(input())
                editNotes(notaest, nota, notaop)
            elif opc == "3":
                print(vernotas(notas))
                print("ingrese el codigo de la nota")
                notaest = int(input())
                del notas[notaest]
                print("**************** NOTA ELIMINADA EXITOSAMENTE ******************")
                time.sleep(3)
            if opc == "4":
                print(menuNotas(notas))
                print("ingrese el codigo de la nota")
                nota = input()
                print("ingrese la nota")
                notaest = int(input())
                count = 0
                pas = True
                for y in notas:
                    if notas[y]["materia"] == notas[nota]["materia"] and y != nota:
                        if notas[y]["nota1"] == "p" and notas[nota]["nota1"] != "p":
                            pas = False
                            break
                        elif notas[y]["nota2"] == "p" and notas[nota]["nota2"] != "p":
                            pas = False
                            break
                        elif notas[y]["nota3"] == "p" and notas[nota]["nota3"] != "p":
                            pas = False
                            break
                if pas == False:
                    print("error no puede guardar la nota todavia")
                    time.sleep(3)
                    break
                for i in notas[nota].keys():
                    if i == "nota1" and notas[nota][i] == "p":
                        notas[nota][i] = notaest
                        notaest = "p"
                    elif i == "nota2" and notas[nota][i] == "p":
                        notas[nota][i] = notaest
                        notaest = "p"
                    elif i == "nota3" and notas[nota][i] == "p":
                        notas[nota][i] = notaest
                        notaest = "p" 
                if notas[nota]["nota1"] != "p" and notas[nota]["nota2"] != "p" and notas[nota]["nota3"] != "p": 
                    notas[nota]["notaf"] = round(sum(x for x in [notas[nota]["nota1"], notas[nota]["nota2"], notas[nota]["nota3"]]) / 3, 2)
                with open("notas.json", "w") as archivo: json.dump(notas, archivo)
            if opc == "5":
                print(verEstudiantes(dicEstudiante))
                print("ingrese el codigo del estudiante")
                id_est = int(input())
                print(showByEst(id_est, notas))
                time.sleep(3)
            print(menuNotas(notas))
            opc = input()
#MENU1
    elif opcMenu == "2":
        print(menuestudiantes(dicEstudiante))
        opc = input()
        while opc != "0":
            if opc == "1":
                print("==================== AGREGAR =================")
                print("ingrese el nombre")
                nombre = input()
                print("ingrese el apellido")
                apellido = input()
                print("ingrese el correo")
                correo = input()
                with open("estudiante.json", "w") as archivo: json.dump(agregarEstudiante(dicEstudiante, nombre, apellido, correo), archivo)
                print("**************** MATERIA EDITADA EXITOSAMENTE ******************")
                time.sleep(3)
            elif opc  == "2":
                print("==================== EDITAR =================")
                print("determine el codigo del estudiante que desea editar: ")
                codigo = int(input())
                print("ingrese el nombre del estudiante")
                dicEstudiante[codigo]["nombres"] = input()
                print("ingrese el apellido del estudiante")
                dicEstudiante[codigo]["apellidos"] = input()
                print("ingrese el correo del estudiante")
                dicEstudiante[codigo]["correo"] = input()
                print("**************** MATERIA EDITADA EXITOSAMENTE ******************")
                time.sleep(3)
            elif opc == "3":
                print("==================== ELIMINAR =================")
                print("determine el codigo del estudiante que desea eliminar: ")
                cod = input()
                del dicEstudiante[cod]   
                with open("estudiante.json", "w") as archivo: json.dump(dicEstudiante, archivo)
            print(menuestudiantes(dicEstudiante))
            opc = input()
    elif opcMenu == "3":
        menumaterias(dicMaterias)
        opc = input()
        print("")
        while opc != "0":
            if opc == "1":
                print("==================== AGREGAR =================")
                print("ingrese el nombre de la materia")
                nombre = input()
                dicMaterias = agregarMateria(dicMaterias, nombre)
                print("**************** MATERIA AGREGADA EXITOSAMENTE ******************")
                time.sleep(3)
            elif opc == "3":
                print("==================== EDITAR =================")
                print("determine el codigo de la materia que desea editar: ")
                codigo = int(input())
                print("ingrese el nombre de la materia")
                dicMaterias[codigo]["nomMateria"] = input()
                print("**************** MATERIA EDITADA EXITOSAMENTE ******************")
                time.sleep(3)
            elif opc == "2":
                print("==================== ELIMINAR =================")
                print("determine el codigo de la materia que desea eliminar: ")
                cod = int(input())
                del dicMaterias[cod]
                with open("notas.json", "w") as archivo: json.dump(dicMaterias, archivo)
            elif opc == "4":
                print(verMaterias(dicMaterias))
            menumaterias(dicMaterias)
            opc = input()
    elif opcMenu == "4":
        print("")
    else:
        print("Por favor ingrese una opcion valida")
