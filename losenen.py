import random
vida_maxima = 100
personaje_protagonistas = {
    "nombre" : "",
    "vida_maxima" : vida_maxima,
    "vida_minima" : vida_maxima,
    "fuerza" : 0,
    "suerte" : 0,
    "monedas": 0,
    "pociones": 0,
    "arma" : {},
    "armadura" : {}
}

armas = {
    "espada" : {
        "daño" : 60,
        "critico" : 120,
        "precio" : 1500
    },
    "arco" : {
        "daño" : 30,
        "critico" : 50,
        "precio" : 1500 
    },
    "tortura medieval" : {
        "daño" : 1000,
        "critico" : 10000,
        "precio" : 1
    }
}

armadura = {
    "casco" : {
        "resistencia" : 100,
        "precio" : 2700
    },
    "pechera" : {
        "resistencia" : 180,
        "precio" : 2300
    },
    "armadura de maicra" : {
        "resistencia" : 1,
        "precio" : 10000
    }
}

pociones = {
    "pocion": {
        "cura": 50,
        "precio": 100
    }
}

enemigos = {
    "arquero" : {
        "vida" : 100,
        "daño" : 18,
        "drops" : 2000,
    },
    "caballero" : {
        "vida" : 200,
        "daño" : 23,
        "drops" : 2300
    },
    "el sufrimiento de la deidad" : {
        "vida" : 10,
        "daño" : 100,
        "drops" : 100
    }
}

def generar_personaje(nombre):
    global personaje_protagonistas
    personaje = personaje_protagonistas.copy()
    personaje["nombre"] = nombre
    personaje["fuerza"] = random.randint(1, 100)
    personaje["suerte"] = random.randint(1, 100)
    mostrar_personaje(personaje)
    return personaje

def mostrar_personaje(personaje: dict):
    print("nombre:", personaje["nombre"])
    print("vida:", personaje["vida_minima"]), "/",  personaje["vida_maxima"]
    print("fuerza:", personaje["fuerza"])
    print("suerte:", personaje["suerte"])
    print("monedas:", personaje["monedas"])
    print("pociones:", personaje["pociones"])
    if personaje["arma"] != {}:
        print("arma ")
        mostrar_arma(personaje["arma"])
    if personaje["armadura"] != {}:
        print("armadura ")
        mostrar_armadura(personaje["armadura"])

def mostrar_arma(arma: dict):
    print("daño:", arma["daño"])
    print("crítico:", arma["critico"])
    print("precio:", arma["precio"])

def mostrar_armadura(armadura: dict):
    print("resistencia:", armadura["resistencia"])
    print("precio:", armadura["precio"])

def curar_personaje(personaje):
    if personaje["pociones"] <= 0:
        print("no tenes pociones")
        return
    if personaje["vida_minima"] >= personaje["vida_maxima"]:
        print("para flaco cuanto mas queres")
        return
    cura = pociones["pocion"]["cura"]
    vida_anterior = personaje["vida_minima"]
    personaje["vida_minima"] = personaje["vida_minima"] + cura
    if personaje["vida_minima"] > personaje["vida_maxima"]:
        personaje["vida_minima"] = personaje["vida_maxima"]
    personaje["pociones"] -= 1
    print("te curaste", personaje["vida_minima"] - vida_anterior, "puntos de vida")
    print("vida:", personaje["vida_minima"], "/", personaje["vida_maxima"])

def tienda(personaje):
    while True:
        print("tianguis")
        print("1) compra armas")
        print("2) compra cosa que te ayudan a la resistencia pa")
        print("3) compra pocion")
        print("4) RAJA DE ACA")
        opcion = int(input("elegi...: "))
        if opcion == 4:
            return
        if opcion < 1 or opcion > 3:
            print("opcion invalido")
            continue
        if opcion == 1:
            cosas = armas
        elif opcion == 2:
            cosas = armadura
        else:
            cosas = pociones
        numero = 1
        for nombre in cosas:
            articulo = cosas[nombre]
            print(numero, ")", nombre, "-", articulo["precio"], "monedas")
            numero = numero + 1
        eleccion = int(input("elegi que queres comprar: "))
        if eleccion < 1 or eleccion > len(cosas):
            print("opcion invalido")
            continue
        numero = 1
        for nombre in cosas:
            if numero == eleccion:
                nombre_producto = nombre
            numero = numero + 1
        articulo = cosas[nombre_producto]
        if personaje["monedas"] < articulo["precio"]:
            print("q haces no podes comprar eso pobre")
            continue
        personaje["monedas"] -= articulo["precio"]
        if opcion == 1:
            personaje["arma"] = cosas[nombre_producto].copy()
        elif opcion == 2:
            personaje["armadura"] = cosas[nombre_producto].copy()
        else:
            personaje["pociones"] += 1
        print("bien papaaaa compraste", nombre_producto, "te quedan", personaje["monedas"], "monedas")

def elegir_enemigo():
    global enemigos
    num = random.randint(1, 3)
    if num == 1:
        return enemigos["arquero"].copy()
    elif num == 2:
        return enemigos["caballero"].copy()
    elif num == 3:
        return enemigos["el sufrimiento de la deidad"].copy()