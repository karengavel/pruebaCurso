import random


def elegirPalabra():
    listaPosibilidades = ["mañana", "tarde", "noche", "atardecer", "sol", "luna"]
    return random.choice(listaPosibilidades)

def pedir_letra():
    letra_elegida = ''
    es_valida = False
    abecedario = 'abcdefghijklmnñopqrstuvwxyz'

    while not es_valida:
        letra_elegida = input("Elige una letra: ")
        if letra_elegida in abecedario and len(letra_elegida) == 1:
            es_valida = True
        else:
            print("No has elegido una letra correcta")
    return letra_elegida

def vidas():
    listaLetrasAdivinadas = []
    listaLetrasErroneas = []
    vidas = 6


    palabra = elegirPalabra()
    print(palabra)
    print("La palabra a encontrar es: ")
    print(' _ ' * len(palabra))

    while True:
        ingreso = pedir_letra()
        if ingreso in listaLetrasAdivinadas or ingreso in listaLetrasErroneas:
            print("Esa letra ya la ingresaste")
        else:
            if ingreso in palabra:
                print("Adivinaste la letra !!!")
                listaLetrasAdivinadas.append(ingreso)
            else:
                print("Está letra no se encuentra oculta :(")
                listaLetrasErroneas.append(ingreso)
                vidas = vidas - 1
                print (f"Has fallado en estas letras: {listaLetrasErroneas}")
                if vidas > 0:
                    print(f"te quedan {vidas} vidas")
                else:
                    print("Has perdido :,(")
                    print(f'La palabra secreta era: {palabra}')
                    break
        estatusActual = ""
        letrasFaltantes = len(palabra)

        for ingreso in palabra:
            if ingreso in listaLetrasAdivinadas:
                estatusActual = estatusActual + ingreso
                letrasFaltantes= letrasFaltantes-1
            else:
                estatusActual = estatusActual + "_"
        print(estatusActual)
        if letrasFaltantes==0:
            print("Felicidades has ganado!!! ")
            print(f'La palabra secreta es: {palabra}')
            break


print("Juguemos ahorcado tendrás 6 vidas para adivinar la palabra oculta")
vidas()
# soy el pseudo body
# registro
# h1
