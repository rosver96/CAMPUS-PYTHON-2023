texto=input()
k=int(input())
abc="A B C D E F G H I J K L M N O P Q R S T U V W X Y Z"
letra=abc.split(" ")

cifrad=""
letra1=[]

#LA CASA

x=len(letra)
for c in texto:
    for i in range(x):
        if c==letra[i]:
            if (i+k)>x:
                a=i+k-(x-1)
            else:
                a=i+k
            cifrad=cifrad+letra[a]
            print(cifrad)
        elif c==" ":
            cifrad=cifrad+" "
            print(cifrad)

print(cifrad)