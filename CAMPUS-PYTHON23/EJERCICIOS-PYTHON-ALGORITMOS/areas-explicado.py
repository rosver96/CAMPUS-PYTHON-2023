# int() es una funcion de python para transformar a un entero
# return es una declaracion que devuelve un valor cuando se llama la funcion
# ** el doble asterico se utiliza como el operador de exponente(elevar un numero a una potencia)
# lower() es un metodo para convertir un string en minusculas

def areaCirculo():
    # pedimos al usuario el radio del circulo y lo almacenamos en una variable
    radio = int(input('Digite el radio del circulo: '))
    # procedemos a calcular el area con la formula (radio^2)*PI y lo almacenamos en una variable
    resultado = ( radio ** 2 ) * 3.14
    # devolvemos el resultado para cuando se llame la funcion
    return resultado
    
def areaTriangulo():
    # pedimos al usuario la base y altura y lo almacenamos en una variable
    
    base = int(input('Digite el base del triangulo: '))
    altura = int(input('Digite la altura del triangulo: '))
    # procedemos a calcular el area con la formula (base*altura)/2 y lo almacenamos en una variable
    resultado = ( base * altura ) / 2
    # devolvemos el resultado para cuando se llame la funcion
    return resultado

def areaCuadrado():
    # pedimos al usuario el lado del cuadrado y lo almacenamos en una variable
    lado = int(input('Digite un lado del cuadrado: '))
    # procedemos a calcular el area con la formula lado * lado y lo almacenamos en una variable
    resultado = lado * lado
    # devolvemos el resultado para cuando se llame la funcion
    return resultado

figuraCalcular = input('Que figura deseas calcular: circulo, triangulo, cuadrado: ').lower()

if figuraCalcular == 'circulo':
    # como la funcion nos retorna(return) un dato lo almacenamos en una variable
    resultado = areaCirculo()
    # mostramos en pantalla el valor con un texto 
    print('El area del circulo es: ', resultado)
elif figuraCalcular == 'triangulo':
    # como la funcion nos retorna(return) un dato lo almacenamos en una variable
    resultado = areaTriangulo()
    # mostramos en pantalla el valor con un texto 
    print('El area del triangulo es: ', resultado)
elif figuraCalcular == 'cuadrado':
    # como la funcion nos retorna(return) un dato lo almacenamos en una variable
    resultado = areaCuadrado()
    # mostramos en pantalla el valor con un texto 
    print('El area del cuadrado es: ', resultado)
else:
    # en caso que el usuario digite otra figura le mostramos un mensaje 
    print('lo siento pero el nombre de la figura es incorrecto')