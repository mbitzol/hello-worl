import random
from collections import deque
historial = deque()
print("MENU PRINCIPAL DEL JUEGO")

while True:
    opciones = ['1', '2', '3']
    opcionrandom = random.randint(0, 2)
    respuesta = opciones[opcionrandom]
    print("Seleccione una opcion")
    print("1. Piedra ")
    print("2. Papel ")
    print("3. Tijera")
    print("4. Terminar el juego")
    Eleccion = input("Digite el numero: ")
    print("--------------------------------------------------------------------------------")

    if Eleccion == respuesta:
        print("EMPATE!!")
        historial.append('FUE UN EMPATE!!')
    if (Eleccion == '1'):
        if (respuesta == '2'):
            print("Elegiste PIEDRA")
            print("El sistema eligio PAPEL")
            print("GANA EL SISTEMAA")
            historial.append("Elegiste PIEDRA, El sistemas eligio PAPEL, GANA EL SISTEMA!!")
        elif (respuesta == '3'):
            print("Elegiste PIEDRA")
            print("El sistema eligio TIJERAS")
            print("TU GANAS!!")
            historial.append("Elegiste PIEDRA, El sistemas eligio TIJERAS, TU GANAS!!")
    if (Eleccion == '2'):
        if (respuesta == '3'):
            print("Elegiste PAPEL")
            print("El sistema eligio TIJERAS")
            print("GANA EL SISTEMA")
            historial.append("Elegiste PAPEL, El sistema eligio TIJERAS, GANA EL SISTEMA!!")
        elif (respuesta == '1'):
            print("Elegiste PAPEL")
            print("El sistema eligio PIEDRA")
            print("TU GANAS!!")
            historial.append("Elegiste PAPEL, El sistema eligio PIEDRA, TU GANAS!!")
    if (Eleccion == '3'):
        if (respuesta == '1'):
            print("Elegiste Tijeras")
            print("El sistema eligio PIEDRA")
            print("GANA EL SISTEMA")
            historial.append("Elegiste TIJERAS, El sistema eligio PIEDRA, GANA EL SISTEMA")
        elif (respuesta == '2'):
            print("Elegiste Tijeras")
            print("El sistema eligio PAPEL")
            print("TU GANAS!!")
            historial.append("Elegiste TIJERAS, El sistema eligio PAPEL, TU GANAS!!")
    print('-------------------------------------------------------------------------------')
    if (Eleccion == '4'):
        break
    while True:
        print("SUBMENU DEL JUEGO")
        print('Deseas?')
        print('1. Volver a jugar')
        print('2. Ver resultado anterior')
        print('3. Salir del submenu')
        volver = input("Digite el numero: ")
        print("-------------------------------------------------------------------------------")

        if volver == '2':
            ultimoresultado = historial.pop()
            print(f'Historial del resultado anterior: {ultimoresultado}')
            if len(historial) == 0:
                print('El historial esta vacio!!')
            print('--------------------------------------------------------------------')
        elif volver == '3' or volver == '1':
            break