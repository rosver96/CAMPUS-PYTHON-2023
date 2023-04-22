#Entero
def validaEntero(etiqueta):
    while True:
        try:
            dato=int(input(etiqueta))
            break
        except:
            print("El dato debe ser un entero ")
    return dato

#Float
def validaFloat(etiqueta):
    while True:
        try:
            dato=float(input(etiqueta))
            break
        except:
            print("El dato debe tener decimales ")
    return dato

#D o H
def validaNatura():
    while True:
        try:
            tipo=input("Naturaleza de la cuenta (D: Debito H: Credito): ")
            if tipo!="D" and tipo!="H":
                print("La naturaleza de la cuenta debe ser D o H ")
                continue
            break
        except ValueError:
            print("La naturaleza de la cuenta debe ser D o H ")
    return tipo

#Dice si es D o H
def addSaldo(tipoMovimiento,saldo,valorMovimiento,naturaleza):
    if tipoMovimiento==naturaleza:
        saldo=saldo+valorMovimiento
    else:
        saldo=saldo-valorMovimiento
    return saldo

#Suma totales segun D o H
def sumaTotal(naturaleza,saldo,sumaD,sumaH):
    if naturaleza=="D":
        sumaD=sumaD+saldo
    else:
        sumaH=sumaH+saldo
    return sumaH,sumaD

#Para movimiento D o H
def validaMovimiento():
    while True:
        try:
            tipo=input("Tipo de movimiento (D: Debito H: Credito): ")
            if tipo!="D" and tipo!="H":
                print("El movimiento debe ser D o H")
                continue
            break
        except ValueError:
            print("El movimiento debe ser D o H")
    return tipo

#Suma de cuentas de naturaleza debito
sumaD=0
#Suma de cuentas de naturaleza credito
sumaH=0

#Listas donde se guardan cada dato de las cuentas
codigos=[]
nombres=[]
naturalezas=[]
saldos=[]

print(" ")
N=validaEntero("Ingrese el numero de cuentas del plan de cuentas de la empresa: ")
print(" ")
for i in range(N):
    codigo=validaEntero("Codigo cuenta: ")
    nombre=input("Nombre cuenta: ")
    naturaleza=validaNatura()
    saldo=validaFloat("Saldo de la cuenta al inicio del mes: ")
    print(" ")
    M=validaEntero("Cantidad de movimientos del mes de la cuenta: ")
    print(" ")
    for i in range(M):
        fecha=input("Fecha del movimiento: ")
        tipoMovimiento=validaMovimiento()
        valorMovimiento=validaFloat("Valor del movimiento: ")
        saldo=addSaldo(tipoMovimiento,saldo,valorMovimiento,naturaleza)
        print(" ")
    sumaH,sumaD=sumaTotal(naturaleza,saldo,sumaD,sumaH)
    codigos.append(codigo)
    nombres.append(nombre)
    naturalezas.append(naturaleza)
    saldos.append(saldo)

print(" ")
print("A continuacion se describe para cuenta el código, nombre, naturaleza y saldo final:")
print(" ")
for i in range(N):
    print(f"Codigo: {codigos[i]}; Nombre: {nombres[i]}; Naturaleza: {naturalezas[i]}; Saldo final: {saldos[i]:,.2f}")
    print(" ")

print(f"Suma de los saldos finales de las cuentas de naturaleza D (Débito): {sumaD:,.2f}")
print(f"Suma de los saldos finales de las cuentas de naturaleza H (Crédito): {sumaH:,.2f}")

        