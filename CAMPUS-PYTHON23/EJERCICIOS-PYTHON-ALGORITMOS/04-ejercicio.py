# 4.Crea una aplicación que nos convierta una cantidad de pesos introducida por teclado a otra
# moneda, estas pueden ser a dolares, yenes o libras. La función tendrá como parámetros, la
# cantidad de pesos y la moneda a pasar que será un texto



pesos = float(input("ingrese un valor en pesos colombianos: "))

def convertir (pesos):
   resultado = pesos/5000
   return resultado

resultado = convertir(pesos)
print(resultado)
    