print("\n\n")
print("\n\n")
import json



# {
#     "bookstore": {
#         "book": [
#             {
#                 "title": {
#                     "_lang": "en",
#                     "__text": "Everyday Italian"
#                 },
#                 "author": "Giada De Laurentiis",
#                 "year": "2005",
#                 "price": "30.00",
#                 "_category": "COOKING"
#             },
#             {
#                 "title": {
#                     "_lang": "en",
#                     "__text": "Harry Potter"
#                 },
#                 "author": "J K. Rowling",
#                 "year": "2005",
#                 "price": "29.99",
#                 "_category": "CHILDREN"
#             },


link = "/home/arteN01-063/Desktop/Progrmacion J.J.L.A/ARCHIVOS TELEFONICOS/Biblioteca.json"


def menu ():
    print("\n¿QUE DESEAS REALIZAR?\n\n 1. VER LIBROS \n 2. AGREGAR NUEVO LIBRO \n 3. EDITAR DATOS DE LIBRO \n 4. BORRAR DATOS DE LIBRO\n 0. FINALIZAR \n")


def lista():
    with open(link, "r") as archivo:
        lista = json.load(archivo)
    archivo.close()
    print('\n************************************************** LISTA **************************************************\n')
    y = len(lista["bookstore"]["book"])
    listaPaciente='NOMBRE'+'\t'+'\t'+'\t'+'IDIOMA'+'\t'+'\t'+'AUTOR'+'\t''\t'+'AÑO'+'\t''\t'+'PRECIO'+'\t'+'\t''CATEGORIA'+'\n\n'
    for i in range(y):
        listaPaciente+=lista["bookstore"]["book"][i]['title']["__text"]+'\t'+lista["bookstore"]["book"][i]['title']["_lang"]+'\t'+str(lista["bookstore"]["book"][i]["author"])+'\t'+str(lista["bookstore"]["book"][i]["year"])+'\t'+'\t'+str(lista["bookstore"]["book"][i]["price"])+'\t'+'\t'+str(lista["bookstore"]["book"][i]["_category"])+'\n'
    print(listaPaciente)




def agregar():
    print("\n NOMBRE DEL LIBRO")
    nombre = input()
    print("\n IDIOMA DEL LIBRO")
    idioma = input()
    print("\n AUTOR DEL LIBRO")
    autor= input()
    print("\n AÑO DEL LIBRO")
    año = input()
    print("\n PRECIO DEL LIBRO")
    precio = input()
    print("\n CATEGORIA DEL LIBRO")
    categoria= input()
    

    with open(link, "r") as archivo:
        dic = json.load(archivo)
        dic["bookstore"]["book"].append({
                 "title": {
                     "_lang": idioma,
                     "__text": nombre
                 },
                 "author": autor,
                 "year": año,
                 "price": precio,
                 "_category": categoria})

    with open(link, "w") as archivo:  
        json.dump(dic,archivo)
    

def editar(titulo):
    with open(link, 'r') as archivo:
        biblioteca = json.load(archivo)
    for libro in biblioteca['bookstore']['book']:
        if libro['title']['__text'] == titulo:
                print("¿QUE DATO DESEAS ACTUALIZAR?\n")
                print("1. AUTOR")
                print("2. AÑO")
                print("3. PRECIO")
                print("4. CATEGORIA")
                opcion = input()
                if opcion == "1":
                    autor = input("INGRESA EL NUEVO NOMBRE DE AUTOR\n")
                    libro['author'] = autor
                elif opcion == "2":
                    year = input("INGRESE EL NUEVO AÑO\n")
                    libro['year'] = year
                elif opcion == "3":
                    price = input("INGRESE EL NUEVO PRECIO\n")
                    libro['price'] = price
                elif opcion == "4":
                    categoria = input("INGRESE LA NUEVA CATEGORIA\n")
                    libro['_category'] = categoria
                else:
                    print("Opción inválida\n")
                    return
            
                print(f"Los datos del libro {titulo} se han actualizado correctamente\n")
                break
    else:
        print(f"No se encontró un libro con el título {titulo}")
        
    with open(link, 'w') as archivo:
        json.dump(biblioteca, archivo, indent=4)


def borrar(titulo):
    with open(link, 'r') as archivo:
        biblioteca = json.load(archivo)
    for libro in biblioteca['bookstore']['book']:
        if libro['title']['__text'] == titulo:
            libro.delete()
            print("LE LIBRO A SIDO BORRADO")

menu()

inicio =int(input())

while inicio!=0:
    if inicio == 1:
        lista()
    elif inicio == 2:
        agregar()
    elif inicio == 3:
        print("CUAL ES EL TITULO DEL LIBRO")
        x = input()
        editar(x)
    elif inicio == 4:
        print("CUAL ES EL TITULO DEL LIBRO")
        x = input()
        borrar(x)

    else:
        print("OPCION INCORRECTA")
    menu()
    inicio =int(input())