# Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario 
# por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada 
# en la variable sin tener en cuenta mayúsculas y minúsculas.

print("\n\n")
password = "contraseña"

user= input("ingrese la contraseña: ")
if password == user.lower():
    print("el pass es el correcto :) ")
else:
    print("el pass esta errado :( ")
