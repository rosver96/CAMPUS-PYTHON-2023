import math
operador = True

while operador == True :
    print("1).circulo \n2).cuadrado \n3).triangulo \n4).trapecio\n5).paralelograma")
    operador = input ( ":)-")

    if operador == "1" :
        radio = int(input("ingrese el numero del radio : "))     # ,(3.1416 * radio) *radio)
        print(" el radio  es: " ,math.pi * radio *radio)        # ,math.pi * radio *radio)
        x = print("presione ENTER para salir....")
        opera = bool(operador)
    if operador == "2" :
        area = int(input("ingrese el numero del area : "))       # ,area*area)  formula
        print(" el area  es: " , area*area)
        x = print("presione ENTER para salir....")
        opera = bool(operador)
    if operador == "3" :
        base = int(input("ingrese una base : "))
        altura = int(input("ingrese una altura : "))             # ,(base*altura) /2 ) formula
        print(" el area  es : " , (base*altura) /2 )  
        x = print("presione ENTER para salir....")
        opera = bool(operador)
    if operador == "4" :
        baseM = int(input("ingrese la base mayor : "))
        basem = int(input("ingrese la base menor : "))
        altura = int(input("ingrese la altura : "))               # ,(baseM + basem) /2*altura )  formula
        print(" el area  es : " , (baseM + basem) /2*altura )
        x = print("presione ENTER para salir....")
        opera = bool(operador)
    if operador == "5" :
        base = int(input("ingrese la base mayor : "))
        altura = int(input("ingrese la altura : "))               #  (base*altura ))    formula
        print(" el area  es : " , (base*altura ))
        x = print("presione ENTER para salir....")
        opera = bool(operador)
