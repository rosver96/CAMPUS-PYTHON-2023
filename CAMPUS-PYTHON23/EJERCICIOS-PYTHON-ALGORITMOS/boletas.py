# para un concierto hay 3 tipos de boletas ,desarrollar un programa que calcule el total de ventas para cada boleta 
# (cuantas boletas se vendieron de cada tipo y cuanto se recaudo por cada boleta) en cada venta se puede vender mas de una boleta 
# ,pero solo de un mismo tipo.
# ubicacion valor us$
# 1).general = 50
# 2).vip   = 75
# 3).platinum = 100 

print("\n\n")
general = 50
vip   = 75
platinum = 100 
numBoletas = 0
contadorG = 0
contadorV = 0
contadorP =0


op = True

while op == True:
    print("*-*.bienvenido que tipo de boleta desea comprar\n1):boleta general \n2).boleta vip \n3).boleta premium")
    op = input ( ":)-")

    if op == "1" :
        numBoletas = int(input("ingrese la cantidad de boletas a comprar: "))
        print(f"se realizo la compra de {numBoletas} en localidad general. ")
        totalGeneral = numBoletas
        contadorG += numBoletas
        op = bool(op)
    elif op == "2" :
        numBoletas = int(input("ingrese la cantidad de boletas a comprar: "))
        print(f"se realizo la compra de {numBoletas} en localidad vip. ")
        totalGeneral = numBoletas
        contadorV += numBoletas
        op = bool(op)
    elif op == "3" :
        numBoletas = int(input("ingrese la cantidad de boletas a comprar: "))
        print(f"se realizo la compra de {numBoletas} en localidad platinum. ")
        totalGeneral = numBoletas
        contadorP += numBoletas
        op = bool(op)

print("total de ventas para las boletas general es: ",general*contadorG)
print("el numero de boletas en localidad general fueron: ",contadorG)
print("total de ventas para las boletas vip es: ",vip*contadorV)
print("el numero de boletas en localidad general fueron: ",contadorV)
print("total de ventas para las boletas platinum es: ",platinum*contadorP)
print("el numero de boletas en localidad general fueron: ",contadorP)