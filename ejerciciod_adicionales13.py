import random

def jugar_ahorcado():
    palabras = ["python", "programacion", "funciones", "ciclos", "computadora", 
                "desarrollador", "algoritmo", "variable"]
    
    palabra_secreta = random.choice(palabras).lower()
    letras_adivinadas = set()
    intentos = 6
    letras_palabra = set(palabra_secreta)
    
    print("¡Bienvenido al Ahorcado!")
    print(f"Palabra de {len(palabra_secreta)} letras")
    
    while intentos > 0:
        # Mostrar progreso
        progreso = [letra if letra in letras_adivinadas else "_" for letra in palabra_secreta]
        print("\nPalabra:", " ".join(progreso))
        print(f"Intentos restantes: {intentos}")
        print(f"Letras usadas: {sorted(letras_adivinadas)}")
        
        if "_" not in progreso:
            print(f"¡Ganaste! La palabra era: {palabra_secreta}")
            return
        
        letra = input("\nIngresa una letra: ").lower().strip()
        
        if len(letra) != 1 or not letra.isalpha():
            print("Ingresa solo una letra")
            continue
        
        if letra in letras_adivinadas:
            print("Ya usaste esa letra")
            continue
        
        letras_adivinadas.add(letra)
        
        if letra not in letras_palabra:
            intentos -= 1
            print(f"❌ La letra '{letra}' no está en la palabra")
    
    print(f"\n¡Perdiste! La palabra era: {palabra_secreta}")

jugar_ahorcado()
