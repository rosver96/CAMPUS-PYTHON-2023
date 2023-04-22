def factorial(numero):
    # por defecto el resultado va hacer 1
    # resultado no debe ser 0 porque vamos a multiplicar el n factorial
    resultado = 1
    while numero > 1:
        # mientras el numero ingresado sea mayor a 1 multiplicamos el numero con lo que tenemos guardo
        # tener en cuenta que la expresion resultado *= numero es lo mismo que resultado = resultado * numero 
        resultado *= numero
        # ahora le restamos 1 al numero para continuar con el bucle
        numero -= 1
    return resultado

# pedimos un numero y lo guardamos luego mostramos en consola pasando la funcion y el dato que habiamos guardamos 
numero = int(input('Digite un numero: '))
print(factorial(numero))