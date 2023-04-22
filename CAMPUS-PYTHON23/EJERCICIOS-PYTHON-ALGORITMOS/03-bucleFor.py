persona = ["juan manuel","jose","lina maria","JOSEFINA"]

persona = ["JUAN",1.75,17]

num = [[2,8,6,5],[5,6,4,4],[4,5,9,7]]

print(num)
num[0][2]=15
print(num)
num.append([5,6,8,7])
print("\n\n")
num[0].append(2)
print(num)

###########  bucle for #################################
print("\n\n")

for i in range(4):
    print(persona[i])
    
########### recorrer valor por valor ############
print("\n\n")

for i in range(3):
    for j in range(4):
        print(num[i][j])
