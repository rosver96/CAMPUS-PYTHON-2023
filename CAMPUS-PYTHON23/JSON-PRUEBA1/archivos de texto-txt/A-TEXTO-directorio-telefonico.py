# 2.Escribir un programa para gestionar un listado telefónico con los nombres y los teléfonos de los clientes de una empresa.
# El programa debe incorporar funciones para: 1. crear el archivo si este no existe, 2. para consultar el teléfono de un cliente, 
# 3. añadir el teléfono de un nuevo cliente y 4. eliminar el teléfono de un cliente. El listado debe estar guardado en el archivo 
# de texto Directorio.txt donde el nombre del cliente y su teléfono deben aparecer separados por comas y cada cliente en una línea distinta.

print("\n\n")

import os 

print("************************ DIRECTORIO TELEFONICO ***************************************")

def crearArchivo ():
    if not os.path.exists("Directorio.txt"):
        documento = open ("Directorio.txt","w")
        documento.close()
    
def consultarTelefono(nombrecliente):
    documento = open ("Directorio.txt","r")
    clientes = documento.readlines()
    for i in clientes:
        if nombrecliente in i:
            print(i)
    documento.close()
    
def añadirTelefono():
    documento = open ("Directorio.txt","a")
    nombr = input("ingrese el nombre del cliente: ")
    telef = input("ingrese el telefono del cliente: ")
    documento.write("\n")
    documento.write(nombr)
    documento.write( " , ")
    documento.write(telef)
    documento.close()

def eliminarTelefono(nombrecliente):
    documento = open ("Directorio.txt","r")
    clientes = documento.readlines()
    documento.close()
    documento = open ("Directorio.txt","w")
    for i in clientes:
        if nombrecliente not in i:
            documento.write(i)
    documento.close()
        
def Menu ():
    
    print("\n1).crear el archivo\n2).consultar el teléfono de un cliente\n3).añadir el teléfono de un cliente\n4).eliminar el teléfono de un cliente")  
Menu()

opc = int(input())

while opc != 5:
    if opc == 1:
        crearArchivo()
    elif opc == 2:
        consultarTelefono(input("ingrese nombre: "))
    elif opc == 3:
        añadirTelefono()
    elif opc == 4:
        eliminarTelefono(input("ingrese nombre: "))
    else:
        print("ingrese una opcion valida")
        
    Menu()
    opc = int(input())
