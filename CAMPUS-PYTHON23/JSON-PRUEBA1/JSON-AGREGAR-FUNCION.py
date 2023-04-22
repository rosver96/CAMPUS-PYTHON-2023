def agregar():
    print("************************ AGREGAR ***************************************\n")
    agregados = int(input("cuantos empleados desea agregar?: "))
    for i in range(agregados):
        id = i+1
        nombre = input("ingrese su nombre: ")
        edad = int(input("ingrese su edad: "))
        numero = int(input("ingrese el numero de telefono: "))

    dic_empresa["personas"].append({"id":id,"nombre": nombre,"edad": edad,"numero": numero})
    with open ("dic_empresa.json","w") as archivo:
        json.dump(dic_empresa,archivo)
        archivo.close()
