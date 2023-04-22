print("\n\n")

# funcion basica.........
def saludar():
    print(" hola a todos")


# funcion con parametros......
def verNombreCompleto(nombre,apellido):
    print(nombre,apellido)


#funcion con parametros y retorno
def obtenerNombreCompleto(nombre,apellido):
    return nombre + " " + apellido

print("\n funcion basica")
saludar()

print("\n funcion con parametros")
verNombreCompleto("maria alejandra", "diaza")

print("\n funcion con parametros y retorno")
nombreCompleto = obtenerNombreCompleto("maria luisa","nuñez")
print(nombreCompleto)
print("\n\n")



