import json


empresa = {

    "personas": [
    ]
}

def cargar():
    try:
        with open("./diccionarioEmpresa.json","r") as archivo :
            empresa = json.load(archivo)
    except FileNotFoundError:
        empresa = {
            "personas": []
        }
    return empresa            

def guardar(diccionario):
    with open("./diccionarioEmpresa.json" ,"w") as archivo :
        json.dump(diccionario, archivo)
    archivo.close() 

# Función para generar un ID único
def generar_id(empresa):
    if "personas" not in empresa:
        empresa["personas"] = []
        return 1
    else:
        ids = [persona["id"] for persona in empresa["personas"]]
        if not ids:
            return 1
        else:
            return max(ids) + 1



def agregarPersona(id):
    
    print("Ingrese su nombre : ")
    nombre = input()
    print("Ingrese su edad: ")
    edad = int(input())
    print("Ingrese su numero de documento: ")
    numero = int(input())

    empresa["personas"].append({"id": id, "nombre": nombre, "edad" : edad, "numero": numero})

def eliminarPersona(empresa, id):
    for persona in empresa :
        if persona["id"] == id :
            empresa["personas"].remove(id)



def verPersonas(empresa):
    print("********* LISTADO DE PERSONAS *********\n")
    print("CÓDIGO\t\t\tNOMBRE\t\t\tEDAD\t\t\tNUMERO DE DOCUMENTO")

    with open("./diccionarioEmpresa.json" ,"r") as archivo :
        empresa = json.load(archivo)
    for persona in empresa["personas"]:
        print(persona["id"],"\t\t\t",persona["nombre"],"\t\t\t", persona["edad"],"\t\t\t",persona["numero"])
    archivo.close()    
    


def verMenu():
    print ("\n\n")
    
    print("********** EMPRESA **********\n")
    print('''Selecciones alguna de las siguientes opciones: 
    1. Agregar persona                  2. Editar persona
    3. Eliminar persona                 4. Listar todas las personas
    5. Salir
    ''')

# actualizar(empresa)
verMenu()

opcion = int(input())

while opcion != 0:

    if opcion == 1:
        agregarPersona(generar_id(empresa))
    elif opcion == 2:
        id = int(input("Ingrese el id de la persona que quiere eliminar"))
        eliminarPersona(empresa,id)
    elif opcion == 4:
        verPersonas(empresa)    
    verMenu()
    opcion = int(input())
    
    
    
    
    # print("--------- Agregar Camper ------------")

    
    # print("Ingrese su nombre : ")
    # empresa["personas"][id]["nombre"]= input()

    # print("Ingrese su edad: ")
    # empresa["estudiantes"][id]["edad"]= int(input())

    # print("Ingrese su numero: ")
    # empresa["estudiantes"][id]["grupo"]= input()    
