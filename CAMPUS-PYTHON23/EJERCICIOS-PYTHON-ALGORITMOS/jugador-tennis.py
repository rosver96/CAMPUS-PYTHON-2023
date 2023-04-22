
jugador1 = input("ingrese el nombre del jugador 1: ").lower()
jugador2 = input("ingrese el nombre del jugador 2: ").lower()

puntuacion= [0,0]

bandera= True

while bandera:
    punto = input("ingrese el nombre del jugador que acabo de anotar, o 's' para salir: ").lower()

    if punto == 's':
        break

    if punto == jugador1:
        puntuacion[0]+=1
    elif punto == jugador2:
        puntuacion[1]+=1
    else:
        print("el jugador ingresado no se encuentra en el juego")

    print("el marcador es:{}-{}".format(*puntuacion))

    if max(puntuacion)>= 6 and max(puntuacion)>= min(puntuacion)+2:
        ganador = jugador1 if puntuacion.index(max(puntuacion))==0 else jugador2
        print(f"{ganador.upper()} gana el set")
        bandera = False