print("\n\n")
# c = n!/((n-r)!r!)
# c = 6!/ ((6-2)!2!)

n = int(input("ingresa el numero n: "))
r = int(input("ingresa el numero r: "))    #no puede ser mayor que n

fn = 1
for i in range(1,n +1):
    fn = fn*i
    
nr = n-r
fnr = 1
for i in range(1,nr +1):
    fnr = fnr*i
    
fr = 1
for i in range(1,r +1):
    fr = fr*i
    
c = fn/(fnr*fr)

print("el resultado es: ",c)


print("\n\n")