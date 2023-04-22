print("\n\n")
dic_categoria = {1:25000, 2:300000, 3:40000, 4:45000, 5:60000,}

n = int(input("ingrese la cantidad dce docentes: "))
total_honorarios = 0

for i in range(n):
    cedula = int(input("ingrese el numero de cedula: "))
    nombre = input("ingrese el nombre: ")
    categoria = int(input("ingrese el categoria: "))
    horas = int(input("ingrese el numero de horas: "))

    honorarios = horas * dic_categoria.get(categoria)        
    total_honorarios += honorarios                           # acumulador 

    print("nombre de docente: ",nombre)
    print("los honorarios son: ",honorarios)
print("total de honorarios: ",total_honorarios)