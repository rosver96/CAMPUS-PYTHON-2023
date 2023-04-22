# 1.Elabore un Programa Python que lea la ruta y nombre de un archivo y muestre por pantalla la línea M del archivo.
# La línea a mostrar también debe ser un dato ingresado por el usuario del programa.
# Si el archivo no existe debe mostrar un mensaje por pantalla informando de ello.

######################################          SIN PEDIR DATOS          ###############################################

import io

try:
    archivo_texto = open("/home/arteN01-062/Desktop/rosver ortiz delgado/El Tigre.txt","r") # para que sirva try la ruta debe estar mal.............
                                                                                            # no es necesario el try ya que el dato es quemado
    tigre = archivo_texto.readlines()

    archivo_texto.close()

    linea = int(input("cual linea quiere ver: "))

    print(tigre[linea])
        
except IOError:
    print("el archivo no existe")


######################################          PIDIENDO LA RUTA CON INPUT     ##########################################

try:
    ruta = input("ingrese la ruta: ")

    archivo_texto = open(ruta,("r"))

    tigre = archivo_texto.readlines()

    archivo_texto.close()

    linea = int(input("que linea desea ver: "))

    print(tigre[linea])
    
except IOError:
    print("el archivo no existe")