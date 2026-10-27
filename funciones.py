from random import randint


def menu():
    print("1) ver informacion del personaje")
    print("2) atacar al enemigo")
    print("3) curar al personaje")
    print("4) comprar armadura, arma o pociones")
    print("5) salir del juego")
    opcion = int(input("ingesa la opcion: "))
    return opcion

def atacar_yes():
    print("1) matar individualmente")
    print("2) modo torre")
    return int(input("escribi su opcion"))

def iniciar_ataque(personaje, enemigo):
    print("pelea no iniciada...")
    while True:
        print("ataca el wacho", personaje["nombre"])
        ataque_base = personaje["fuerza"] + personaje["arma"].get("daño", 0)
        if randint(1, 100) <= personaje["suerte"]:
            print("wow golpe critico!")
            ataque = ataque_base + ataque_base * (personaje["suerte"] / 100)
        else:
            ataque = ataque_base
        enemigo["vida"] -= ataque
        if enemigo["vida"] <= 0:
            recompensa = enemigo.get("drops", 0)
            personaje["monedas"] += recompensa
            print("el enemigo murio sos un asesino de pancho")
            print("RECIBISTE", recompensa, "muchas monedillas tio")
            return True, personaje
        print("apa el enemigo sigue con vida Y COTRAAAATACAAAAAA")
        resistencia = personaje["armadura"].get("resistencia", 0)
        daño_recibido = max(0, enemigo["daño"] - resistencia)
        personaje["vida_minima"] -= daño_recibido
        if personaje["vida_minima"] <= 0:
            print("q nene facha, perdiste")
            return False, personaje
        print("seguis vivito y coleando, pelea gogo")

def jugar_torre(personaje, enemigos_torre):
    numero = 1
    for enemigo in enemigos_torre:
        print("pelea numererelal", numero)
        print("te toca contra...........", enemigo["nombre"])
        gano, personaje = iniciar_ataque(personaje, enemigo)
        if not gano:
            print("pero perdiste en la pelea nene facha", numero, "se acabo tu farsa")
            return
        numero = numero + 1
    print("fua ganaste todas las 5 peleas? q capo")