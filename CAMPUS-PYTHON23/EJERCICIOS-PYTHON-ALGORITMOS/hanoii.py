print("\n\n")

def hanoii (p1,p3,p2,n):
    if n > 1:
        hanoii(p1,p2,p3,n-1)
        hanoii(p1,p3,p2,1)
        hanoii(p2,p3,p1,n-1)
    else:
        print("mover de ",p1,"a",p3)

n=int(input("ingrese un numero: "))
print(n)
hanoii("a","c","b",n)
