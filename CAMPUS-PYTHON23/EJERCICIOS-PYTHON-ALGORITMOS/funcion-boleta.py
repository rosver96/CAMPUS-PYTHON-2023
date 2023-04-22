# para un concierto hay 3 tipos de boletas ,desarrollar un programa que calcule el total de ventas para cada boleta 
# (cuantas boletas se vendieron de cada tipo y cuanto se recaudo por cada boleta) en cada venta se puede vender mas de una boleta 
# ,pero solo de un mismo tipo.
# ubicacion valor us$
# 1).general = 50
# 2).vip   = 75
# 3).platinum = 100 

print("\n\n")
general = 50
totalGeneral = 0
vip   = 75
totalVip = 0
platinum = 100 
totalPremium = 0

totalVentas = 0
numBoletas = 0


op = True

while op == True:
    print("*-*.bienvenido que tipo de boleta desea comprar\n1):boleta general \n2).boleta vip \n3).boleta premium")
    op = input ( ":)-")

    if op == "1" :
        numBoletas = int(input("ingrese la cantidad de boletas a comprar: "))
        numBoletas += general
        print(f"la suma de {numBoletas} + {general} = {numBoletas + general}")
        totalGeneral = numBoletas
        print("total de ventas para las boletas general es: ",numBoletas)
    elif op == "2" :
        numBoletas = int(input("ingrese la cantidad de boletas a comprar: "))
        totalVip = totalVip 
        print("total de ventas para las boletas general es: ",totalVip)
    elif op == "3" :
        numBoletas = int(input("ingrese la cantidad de boletas a comprar: "))
        totalPremium = totalPremium + numBoletas
        print("total de ventas para las boletas general es: ",totalPremium)
    
       

#    prom = (n1+n2+n2)/3
#     estudiantes.append([nombre,n1,n2,n3,prom])
    
    
############################################################################
peracion = True

while operacion == True :
    print("1. suma \n2).resta \n3).multiplicacion \n4).division")
    operacion = input ( ":)-")

    if operacion == "1" :
        v1 = int(input("ingrese un numero1 : "))
        v2 = int(input("ingrese un numero2 : "))
        print(f"la suma de {v1} + {v2} = {v1+v2}")
        x = ("predsione ENTER para salir....")
        operacion = bool(operacion)
    if operacion == "2" :
        v1 = int(input("ingrese un numero1 : "))
        v2 = int(input("ingrese un numero2 : "))
        print(f"resta de {v1} - {v2} = {v1-v2}")
        x = ("predsione ENTER para salir....")
        operacion = bool(operacion)
    if operacion == "3" :
        v1 = int(input("ingrese un numero1 : "))
        v2 = int(input("ingrese un numero2 : "))
        print(f"la multiplicacion de {v1} * {v2} = {v1*v2}")
        x = ("predsione ENTER para salir....")
        operacion = bool(operacion)
    if operacion == "4" :
        v1 = int(input("ingrese un numero1 : "))
        v2 = int(input("ingrese un numero2 : "))
        print(f"la resta de {v1} // {v2} = {v1//v2}")
        x = ("predsione ENTER para salir....")
        operacion = bool(operacion)

############################################################################



