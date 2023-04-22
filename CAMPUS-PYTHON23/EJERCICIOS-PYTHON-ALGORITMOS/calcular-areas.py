# 1.Crea una aplicación que nos calcule el área de un círculo, cuadrado o triangulo.
# Pediremos qué figura queremos calcular, su área y según lo introducido pedirá los valores
# necesarios para calcular el área. Crea una función por cada figura para calcular cada área,
# este devolverá un número real. Muestra el resultado por pantalla
# Circulo: (radio^2)*PI
# Triangulo: (base * altura) / 2
# Cuadrado: lado * lado
def areaCirculo(): 
    radio = int(input('Digite el radio del circulo: ')) 
    resultado = ( radio ** 2 ) * 3.14
    return resultado

def areaTriangulo():
    base = int(input('Digite el base del triangulo: '))
    altura = int(input('Digite la altura del triangulo: '))
    resultado = ( base * altura ) / 2
    return resultado

def areaCuadrado():
    lado = int(input('Digite un lado del cuadrado: '))
    resultado = lado * lado
    return resultado

figuraCalcular = input('Que figura deseas calcular: circulo, triangulo, cuadrado: ').lower()

if figuraCalcular == 'circulo': 
    resultado = areaCirculo()
    print('El area del circulo es: ', resultado)
elif figuraCalcular == 'triangulo':
    resultado = areaTriangulo()
    print('El area del triangulo es: ', resultado)
elif figuraCalcular == 'cuadrado':
    resultado = areaCuadrado()
    print('El area del cuadrado es: ', resultado)
else:
    print('lo siento pero el nombre de la figura es incorrecto')
