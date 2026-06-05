def fibonacci(n):
    """Retorna los primeros n números de la secuencia Fibonacci"""
    if n <= 0:
        return []
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[-1] + fib[-2])
    return fib[:n]


def main_fibonacci():
    print("=== Secuencia de Fibonacci ===")
    try:
        cantidad = int(input("¿Cuántos números de Fibonacci quieres ver? "))
        secuencia = fibonacci(cantidad)
        print(f"Primeros {cantidad} números de Fibonacci:")
        print(secuencia)
    except ValueError:
        print("Ingresa un número válido")


main_fibonacci()
