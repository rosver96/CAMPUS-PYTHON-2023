N=int(input())
cedulas=[]
numeros=[]
valores=[]
gana=[]
num=int(input())

for i in range(N):
    cedula=int(input())
    numero=int(input())
    valor=int(input())
    cedulas.append(cedula)
    numeros.append(numero)
    valores.append(valor)
    gana.append(0)

x=num
y1=x-(x//1000)*1000
y2=y1-(y1//100)*100
y4=y2-(y2//10)*10
n1=0
for i in range(len(cedulas)):
    if num==numeros[i]:
        vp=4000*valores[i]
        gana[i]=2

for i in range(len(cedulas)):
    if numeros[i]!=num:
        x=numeros[i]
        y1=x-(x//1000)*1000
        y2=y1-(y1//100)*100
        y3=y2-(y2//10)*10
        if y4==y3:
            gana[i]=1

suma=0
suma1=0
for i in range(len(cedulas)):
    if gana[i]==2:
        suma=vp+suma
        print(cedulas[i])
        print(vp)

for i in range(len(cedulas)):
    suma1=valores[i]+suma1
    if gana[i]==1:
        print(cedulas[i])
        print(300*valores[i])
        suma=300*valores[i]+suma
    

print(suma1)
print(suma)
        