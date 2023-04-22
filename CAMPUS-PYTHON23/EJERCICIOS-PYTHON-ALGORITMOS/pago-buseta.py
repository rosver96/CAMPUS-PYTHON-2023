nombre=input("Nombre: ")
placa=input("Placa del vehiculo: ")
pasajes=float(input("Valor total por concepto de pasajes: "))
encomiendas=float(input("Valor total por concepto de encomiendas: "))

v_pasajes=pasajes*0.25
v_encomiendas=encomiendas*0.15
valor=pasajes*0.25+encomiendas*0.15

print("Nombre: ",nombre)
print("Placa del vehiculo: ",placa)
print("Valor total pasajes: ",pasajes )
print("Valor a pagar por concepto de pasaje: ",v_pasajes)
print("Valor total encomiendas: ",encomiendas)
print("Valor a pagar por concepto de encomiendas: ",v_encomiendas)
print("Valor total a pagar por el conductor: ",valor)
        
    
    