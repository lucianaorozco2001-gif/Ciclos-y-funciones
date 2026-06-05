def factorial(numero):
    """Calcula el factorial de un número (n!)"""
    if numero < 0:
        return "No se puede calcular factorial de números negativos"
    if numero == 0 or numero == 1:
        return 1
    
    resultado = 1
    for i in range(2, numero + 1):
        resultado *= i
    return resultado


# Prueba interactiva
def main_factorial():
    print("=== Calculadora de Factorial ===")
    try:
        n = int(input("Ingresa un número entero positivo: "))
        print(f"{n}! = {factorial(n)}")
    except ValueError:
        print("Por favor ingresa un número válido")


main_factorial()
