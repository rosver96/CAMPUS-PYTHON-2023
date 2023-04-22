def convertirDolares():
    # pedimos la cantidad de pesos y lo almacenamos en una variable
    pesos = int(input('Digite la cantidad de pesos: '))
    # procedemos a convertir, dividiendo pesos por el equivalente a un dolar y lo almacenamos en una variable
    resultado = pesos / 4752
    # devolvemos el resultado para cuando se llame la funcion
    return resultado
    
def convertirYenes():
   # pedimos la cantidad de pesos y lo almacenamos en una variable
    pesos = int(input('Digite la cantidad de pesos: '))
    # procedemos a convertir, dividiendo pesos por el equivalente a un yen y lo almacenamos en una variable
    resultado = pesos / 36
    # devolvemos el resultado para cuando se llame la funcion
    return resultado

def convertirLibras():
    # pedimos la cantidad de pesos y lo almacenamos en una variable
    pesos = int(input('Digite la cantidad de pesos: '))
    # procedemos a convertir, dividiendo pesos por el equivalente a una libra y lo almacenamos en una variable
    resultado = pesos / 5810
    # devolvemos el resultado para cuando se llame la funcion
    return resultado

monedaConvertir = input('A que moneda deseas convertirlo: dolar, yen, libra: ').lower()

if monedaConvertir == 'dolar':
    # como la funcion nos retorna(return) un dato lo almacenamos en una variable
    resultado = convertirDolares()
    # mostramos en pantalla el valor con un texto 
    print('la conversion en dolares es: ', resultado)
elif monedaConvertir == 'yen':
    # como la funcion nos retorna(return) un dato lo almacenamos en una variable
    resultado = convertirYenes()
    # mostramos en pantalla el valor con un texto 
    print('El area del triangulo es: ', resultado)
elif monedaConvertir == 'libra':
    # como la funcion nos retorna(return) un dato lo almacenamos en una variable
    resultado = convertirLibras()
    # mostramos en pantalla el valor con un texto 
    print('El area del cuadrado es: ', resultado)
else:
    # en caso que el usuario digite otra moneda le mostramos un mensaje 
    print('lo siento pero la moneda es incorrecta')