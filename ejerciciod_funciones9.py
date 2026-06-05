import random


def generar_numero_secreto(minimo, maximo):
    return random.randint(minimo, maximo)


def dar_pista(secreto, intento):
    if intento == secreto:
        return "correcto"
    elif intento < secreto:
        return "más alto"
    else:
        return "más bajo"


def jugar():
    print("¡Adivina el número entre 1 y 100!")
    secreto = generar_numero_secreto(1, 100)
    intentos = 0
    max_intentos = 7
    
    while intentos < max_intentos:
        try:
            intento = int(input(f"\nIntento {intentos+1}/{max_intentos}: "))
            intentos += 1
            
            resultado = dar_pista(secreto, intento)
            
            if resultado == "correcto":
                print(f"¡Felicidades! Adivinaste el número {secreto} en {intentos} intentos.")
                return
            else:
                print(f"Pista: El número es {resultado}")
        except ValueError:
            print("Por favor ingresa un número válido.")
    
    print(f"¡Se acabaron los intentos! El número era {secreto}.")


jugar()