print("\n\n")
from random import randint
abril =[]
mayo = []
junio = []
promabril = 0
prommayo = 0
promjunio = 0

for i in range (31):
    if i<30:
        abril.append(randint(0,11))
        promabril += abril[i]
        mayo.append(randint(0,11))
        prommayo += mayo[i]
        junio.append(randint(0,11))
        promjunio += junio[i]
    else:
        mayo.append(randint(0,11))
        prommayo += mayo[i]

promabril = round(promabril/30,2)
prommayo = round(prommayo/31,2)
promjunio = round(promjunio/30,2)

print("abril\mayo\junio\t")
print(promabril,"\t", prommayo,"\t",promjunio ,"\t")

if promabril > prommayo and promjunio:
    print("abril es el mes mas lluvioso con: ",promabril)
elif prommayo > promabril and promjunio:
    print(" mayo es el mes mas lluvioso con:  ",prommayo)
else:
    print("junio fue el mes mas lluvioso con: ",promjunio)
print("\n\n")
