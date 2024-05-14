import random

from colorama import Fore, Style



def cls():
    print("\n" * 50)

def Juego():
    while True:
        cls()
        print(Fore.RED + "Batalla de dados" + Style.RESET_ALL)
        print("--------------------------------------")
        print("Este juego consiste en una batalla de suerte.")
        print("Ambos jugadores de forma aleatoria sacaran un numero entre 1 y 6.")
        print("Como se contaran los puntos:")
        print("Separación de 0 o 1 entre ambos dados = 0 puntos.")
        print("Separación de 2 o 3 entre ambos dados = 1 puntos.")
        print("Separación de 4 o 5 entre ambos dados = 2 puntos.")
        print("--------------------------------------")
        print("Ejemplo practico")
        print("Dado Jugador 1 = 2.")
        print("Dado Jugador 2 = 5.")
        print("Separacion = 3.")
        print("Resultado = El jugador 2 ha ganado un punto.")

        puntos = int(input("A cuantos puntos quieres jugar: "))

        # Variables de puntos de los jugadores.
        puntosj1 = 0
        puntosj2 = 0

        while puntosj1 < puntos and puntosj2 < puntos:
            cls()

            print("Batalla de Dados")
            print("--------------------------------------")
            print("Puntos Jugador1: " + str(puntosj1))
            print("Puntos Jugador2: " + str(puntosj2))
            print("--------------------------------------")
            print("Jugamos a "+ str(puntos) + " puntos")
            input("Presiona enter para continuar...")
            cls()

            dado1 = random.randint(1, 6)
            dado2 = random.randint(1, 6)

            print("Batalla de Dados")
            print("--------------------------------------")
            print("Dados jugador 1 = " + str(dado1))
            print("Dados jugador 2 = " + str(dado2))
            print("--------------------------------------")
            input("Presiona enter para continuar...")

            Separacion1 = dado1 - dado2
            Separacion2 = dado2 - dado1

            if dado1==dado2:
                print("Resultado = Empate.")

            if dado1>dado2:

    
                if Separacion1==1:
                    print("Separacion = 1")
                    print("Resultado = No se ganan puntos.")
    
                if Separacion1==2:
                    print("Separacion = 2")
                    print("Resultado = Jugador 1 gana un punto.")
                    puntosj1 = puntosj1 + 1
    
                if Separacion1==3:
                    print("Separacion = 3")
                    print("Resultado = Jugador 1 gana un punto.")
                    puntosj1 = puntosj1 + 1
    
                if Separacion1==4:
                    print("Separacion = 4")
                    print("Resultado = Jugador 1 gana dos punto.")
                    puntosj1 = puntosj1 + 2
    
                if Separacion1==5:
                    print("Separacion = 5")
                    print("Resultado = Jugador 1 gana dos punto.")
                    puntosj1 = puntosj1 + 2
    


            if dado2>dado1:

    
                if Separacion2==1:
                    print("Separacion = 1")
                    print("Resultado = No se ganan puntos.")
    
                if Separacion2==2:
                    print("Separacion = 2")
                    print("Resultado = Jugador 2 gana un punto.")
                    puntosj2 = puntosj2 + 1
    
                if Separacion2==3:
                    print("Separacion = 3")
                    print("Resultado = Jugador 2 gana un punto.")
                    puntosj2 = puntosj2 + 1
    
                if Separacion2==4:
                    print("Separacion = 4")
                    print("Resultado = Jugador 2 gana dos punto.")
                    puntosj2 = puntosj2 + 2
    
                if Separacion2==5:
                    print("Separacion = 5")
                    print("Resultado = Jugador 2 gana dos punto.")
                    puntosj2 = puntosj2 + 2
            
            pause = input("Presiona enter para continuar...")

        while puntosj1 >= puntos and puntosj2 >= puntos:
            cls()

        if puntosj1 >= puntos:
            print("Gana Jugador 1")
        if puntosj2 >= puntos:
            print("Gana Jugador 2")
            
            pause = input("Presiona enter para continuar...")
            break
            

        jugar_nuevamente = input("¿Quieres jugar de nuevo? (s/n): ")
        if jugar_nuevamente.lower() != 's':
            break

Juego()