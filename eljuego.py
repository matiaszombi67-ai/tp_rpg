#hay que ver informacion del personaje
#atacar hacia al enemigo
#curar al personaje
#comprar -> armadura -> arma -> pociones<
from enenen.losenen import *
from funciones import *
personaje = generar_personaje(input("ingese el nombre "))

while True:
    opcion = menu()
    if opcion == 1:
        mostrar_personaje(personaje)
    elif opcion == 2:
        opcion = atacar_yes()
        if opcion == 1:
            enemigo = elegir_enemigo()
            iniciar_ataque(personaje, enemigo)
        elif opcion == 2:
            nombres_torre = [
                "arquero",
                "caballero",
                "el sufrimiento de la deidad",
                "arquero",
                "caballero"
            ]
            enemigos_torre = []
            for nombre in nombres_torre:
                enemigo = enemigos[nombre].copy()
                enemigo["nombre"] = nombre
                enemigos_torre.append(enemigo)
            jugar_torre(personaje, enemigos_torre)
    elif opcion == 3:
        curar_personaje(personaje)
    elif opcion == 4:
        tienda(personaje)
    elif opcion == 5:
        break
    else:
        print("y si lo es? Y si es lo que es nada?")