nba = []
opcion = 0
while opcion !=3:
      print("1).registro de jugadores\n2).estadistica por jugador \n3).asistencias \n4).salir")
      opcion = int(input(":)-"))
      if opcion == 1:
        print("registro de jugadores")
        nombreEquipo = input("ingrese nombre del equipo : ")
        nombreJugador = input("ingrese nombre del jugador : ")
        dorsal = int(input("ingrese nro de dorsal :"))
        edad = int(input("ingrese edad :"))
        #0-tiempo jugado, 1-asistencias,2-total canastas,3-total puntos anotados
        nba.append([nombreEquipo,nombreJugador,dorsal,edad,[0,0,0,0]])

      elif opcion == 2:
        equipo = input("ingrese nombre del equipo : ")
        dorsal = int(input("ingrese nro de dorsal : "))
        for item in nba:
            if (equipo in item and dorsal in item):
                item[4][0] += float(input("minutos jugados :"))
      elif opcion == 3:
        equipo = input("ingrese nombre del equipo : ")
        dorsal = int(input("ingrese nro de dorsal : "))
        for item in nba:
            if (equipo in item and dorsal in item):
                item[5][1] += float(input("asistencias :"))
print(nba)





