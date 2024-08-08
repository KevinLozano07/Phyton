from random import randint 

def Puntajes(puntaje , Dado):
    if Dado == 1:
        return 0
    else:
        return puntaje + Dado

def Mostrar_puntajes(Name, Puntaje_player, puntaje_pc):
    print("#" * 60) 
    print(f"El puntaje de {Name} es de {Puntaje_player}")
    print("")
    print(f"El puntaje de computador es de {puntaje_pc}")
    print("#" * 60) 

puntaje_player = 0
Puntajes_pc = 0
x = 1

Bienvenida = """
Bievnenido a Game Dice! 

Un juego de aleatoridad donde te enfentas contra el ordenador
el juego consiste en que se lanzara un dado los resltados 
se iran sumando a medida que se lanze el dado dependiendo de 
quien obtenga un mayor puntaje sera el ganador pero si se llega
a sacar un 1 el puntaje decaera hasta 0, dicho esto
buena suerte y diviertete.
"""

print(Bienvenida)

Name = input("Intrduzca su nombre para comenzar: ")


while x == 1:
    print("")
    input("Presione Enter para lanzar los dados")
    print("")
    Dado_player = randint(1, 6)
    puntaje_player = Puntajes(puntaje_player , Dado_player)

    Dado_pc = randint(1, 6)
    Puntajes_pc = Puntajes(Puntajes_pc, Dado_pc)

    Mostrar_puntajes(Name, puntaje_player, Puntajes_pc)
    print("")

    x = int(input("Si desea volver a jugar presione \"1\" y desea salir presion \"0\" : "))

if puntaje_player > Puntajes_pc:
    print("")
    print(f"{Name} es el ganador con un puntaje de {puntaje_player}")
    print("")
    print(f"El computador perdio con un puntaje de {Puntajes_pc}")
    print("")
else:
    print("")
    print(f"El pc es el ganador con un puntaje de {Puntajes_pc}")
    print("")
    print(f"{Name} perdio con un puntaje de {puntaje_player}")
    print("")