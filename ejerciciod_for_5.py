texto = "Hola Python"

vocales = "aeiouAEIOU"
contador = 0

for letra in texto:
    if letra in vocales:
        contador += 1

print("Cantidad de vocales:", contador)
