def es_primo(numero):
    """Verifica si un número es primo"""
    if numero <= 1:
        return False
    if numero <= 3:
        return True
    if numero % 2 == 0 or numero % 3 == 0:
        return False
    
    i = 5
    while i * i <= numero:
        if numero % i == 0 or numero % (i + 2) == 0:
            return False
        i += 6
    return True


def main_primos():
    print("=== Verificador de Números Primos ===")
    try:
        num = int(input("Ingresa un número: "))
        if es_primo(num):
            print(f"✅ {num} es un número primo")
        else:
            print(f"❌ {num} NO es primo")
    except ValueError:
        print("Ingresa un número entero válido")


main_primos()
