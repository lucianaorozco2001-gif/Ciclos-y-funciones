numero_secreto = 7

intento = int(input("Adivina el número: "))

while intento != numero_secreto:
    if intento < numero_secreto:
        print("Más alto")
    else:
        print("Más bajo")

    intento = int(input("Intenta de nuevo: "))

print("¡Correcto! Adivinaste el número.")