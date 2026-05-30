numeros = [23, 45, 12, 67, 34, 89, 15]

mayor = numeros[0]

for numero in numeros:
    if numero > mayor:
        mayor = numero

print("El número mayor es:", mayor)
