import json

#######################     CREAR ARCHICO JSON CON LISTAS   #################################
#estructura de datos
lista = [10,20,30,40,60]


#fase de apertura y creacion
with open("lista.json","w") as archivo:
    json.dump(lista,archivo)
    
#fase de cierre
archivo.close()


########################   CREAR ARCHICO JSON CON DICCIONARIOS    ################################

#estructura de datos
diccionario = {"1":"lapiz","2":"borrador","3":"cuaderno","4":"lapicero"}


#fase de apertura y creacion
with open("diccionario.json","w") as archivo:
    json.dump(diccionario,archivo)
    
#fase de cierre
archivo.close()


################ LEER UN ARCHIVO JSON PARA RECUPERAR LA ESTUCTURA DE DATOS LISTA  ###################

#fase de apertura y creacion
with open("lista.json","r") as archivo:
    lista=json.load(archivo)
    
#fase de cierre
archivo.close()

print("lista: ",lista)

for i in range (len(lista)):
    print(lista[i])



############## LEER UN ARCHIVO JSON PARA RECUPERAR LA ESTUCTURA DE DATOS DICCIONARIO  ###############

#fase de apertura y creacion
with open("diccionario.json","r") as archivo:
    diccionario=json.load(archivo)
    
#fase de cierre
archivo.close()

print("diccionario: ",diccionario)

print(diccionario["3"])