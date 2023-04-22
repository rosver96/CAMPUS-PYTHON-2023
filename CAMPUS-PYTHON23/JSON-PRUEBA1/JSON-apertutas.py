
# open => nombre(lectura(r))
# write => escribir en el archivo 


#############################   documentos JSON    ##########################################
# importar modulo
import io

# creacion apertura
archivo_texto = open("nombres.txt","w")

# fase manipulacion
nom= "sergio medina \nluisa ruiz \nmario moreno"
archivo_texto.write(nom)

# fase cierre
archivo_texto.close()

print(nom)