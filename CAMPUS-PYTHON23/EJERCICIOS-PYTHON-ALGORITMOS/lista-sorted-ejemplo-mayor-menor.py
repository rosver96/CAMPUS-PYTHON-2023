#     milista.sorted(reverse=True)     coloca los numeros de mayor a menor o los ordena si cambio > o < de mayor o menor cambia el orden

mi_lista = [12,25,63,89,1,6]

n=len(mi_lista)
for i in range(n-1):
    for j in range (i +1,n):
        if mi_lista[i] < mi_lista[j]:
            t = mi_lista[i]
            mi_lista[i] = mi_lista[j]
            mi_lista[j]=t
print(mi_lista)