# determinar en los meses de abril,mayo y junio el promedio de lluvias del mes, teniendo en cuenta los centimetros
# de lluvia caidos por dia (los valores de los centimetros de lluvia por dia pueden ser generados por medio de un 
# numero aleatorio entre 0 y 11) y determinar cual fue el mes mas lluvioso en promedio.

import random

abril =[]
mayo = []
junio = []
promabril =0
prommayo =0
promjunio =0

for i in range(0,30):
    abril.append(random.randint(0,11))
    mayo.append(random.randint(0,11))
    junio.append(random.randint(0,11))
    promedio = (abril + mayo +junio)/3
print(promabril)
print(prommayo)
print(promjunio)
     
if abril > mayo and junio:
    print("el mes mas lluvioso es abril")
elif mayo > abril and junio:
    print("el mes mas lluvioso es mayo")
elif junio > mayo and abril:
    print("el mes mas lluvioso es junio")
else:
    print(" LOS MESES SON IGUALES DE LLUVIOSOS")












