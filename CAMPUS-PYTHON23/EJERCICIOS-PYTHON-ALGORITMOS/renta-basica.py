
n=int(input())
gana=[]
for i in range(n):
    gana.append(0)

nombre=[]
cedula=[]
genero=[]
estrato=[]
ingreso=[]
numero=[]
suma=0

for i in range(n):
    nombre.append(input())
    cedula.append(int(input()))
    genero.append(input())
    estrato.append(int(input()))
    ingreso.append(int(input()))
    numero.append(int(input()))
    if 1500000>=ingreso:
        if estrato==1 and numero>=3:
            gana[i]=1
        elif estrato==2 and numero>=3:
            gana[i]=1

for i in range(n):
    if gana[i]==1:
        if genero[i]=="M":
            suma=suma+1
        print(nombre[i])
        print(cedula[i])

print(len(genero)-suma)
print(suma)
        
    