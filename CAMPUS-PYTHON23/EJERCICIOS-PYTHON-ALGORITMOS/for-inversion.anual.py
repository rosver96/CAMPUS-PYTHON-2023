# Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número 
# de años, y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.

print("\n\n")
invertir = float(input("ingrese la cantidad a invertir: "))
interesAnual = float(input("ingrese el interes: "))
numeroAños= int(input("ingrese el tiempo en años: "))

for i in range(numeroAños):
    invertir *= 1 + interesAnual / 100 
    print("Capital tras " + str(i+1) + " años: " + str(round(invertir, 2)))



# opcion 2 ----------------------------------------------------------------------
amount = float(input("¿Cantidad a invertir? "))
interest = float(input("¿Interés porcentual anual? "))
years = int(input("¿Años?"))
for i in range(years):
    amount *= 1 + interest / 100 
    print("Capital tras " + str(i+1) + " años: " + str(round(amount, 2)))