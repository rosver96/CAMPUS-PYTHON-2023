
fecha =input(" ingrese una fecha dd/mm/aaaa: ")
feb= 0
dias = 0

dia = int(fecha[0:2])
mes = int(fecha[3:5])
año = int(fecha[6:10])

# and (año % 400 == 0 or año % 100 != 0): ..... si esta parte se puede presentar
if año % 4 == 0 and (año % 400 == 0 or año % 100 != 0):
    feb = 29
else:
    feb=28

diasMes = [31,feb,31,30,31,30,31,31,30,31,30,31]
for i in range(mes-1):
    dias += diasMes[i]
dias += dia
print(fecha,"es el dia ",dias, "del año", año)