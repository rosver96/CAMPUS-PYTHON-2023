pcto =""
valor=""
otro=""
total=0
cantidad=0
compras=""
valoresD=[]
verdaderos=""
print("Lisa de compras")

opc=input("Desea agregar el total a la venta \n 1. compras \n 2. ventas \n\n ")

def mostrar():
    i = 0
    while len(valoresD) >= i:
        print()

def others():
    compras=input("\n Ingrese el producto")
    print(compras)
    valor= int(input("Ingrese el valor: $ "))
    total = total + valor
    cantidad = cantidad + 1

if opc=="1":
    compras=input("\n Ingrese el producto")
    print(compras)
    valor= input("Ingrese el valor: $ ")
    valoresD.append(valor)
    print(valoresD)
    total = total +  int(valor)
    cantidad += 1
    while otro == "" or otro == "s" or otro == "S":
        otro =input("\n Desea agregar otro producto? s/n \n")
        if otro =="S" or otro =="s":
            compras= compras +"\n" + input("\n Ingrese el producto")
            print(compras)
            total = total + int(valor)
            valor=input("Ingrese el valor: $ ")
            valoresD.append(valor)
            print(valoresD)
            #valoresD =  valoresD +"\n" + valor
            #valores= valores + "\n" + valor
            cantidad = cantidad + 1
        else:
            pass
        
        verdaderos = verdaderos + "\n\t\t\t\t" + mostrar()
        
    print("\n ************************ COMPRAS ************************")
    print("\nPRODUCTO------------------ \t\t  VALOR------------------ \t\t TOTAL------------------")
    print(f"{compras} \t\t\t\t\t  \r\r{verdaderos} \t\t\t\t\t {total} ")
    print(mostrar())
    print(valoresD)
    print(f"Y compraste {cantidad} productos")
    
    