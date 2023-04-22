# Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales o superiores 
# a 1000 € mensuales. Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales 
# y muestre por pantalla si el usuario tiene que tributar o no.
print("\n\n")

edad = int(input("ingrese su edad: "))
ingresosMensuales= float(input("digite sus ingresos mensuales: "))

if edad >= 16 and ingresosMensuales >= 1000:
    print("cumples los requisitos para tributar")
else:
    print("no cumples los requisitos")