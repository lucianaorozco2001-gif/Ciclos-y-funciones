niveles = 5

for i in range(niveles):
    espacios = " " * (niveles - i - 1)
    asteriscos = "*" * (2 * i + 1)
    print(espacios + asteriscos)
    