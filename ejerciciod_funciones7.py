def analizar_numeros(lista):
    if not lista:
        return {"error": "Lista vacía"}
    
    promedio = sum(lista) / len(lista)
    maximo = max(lista)
    minimo = min(lista)
    pares = sum(1 for x in lista if x % 2 == 0)
    impares = len(lista) - pares
    
    return {
        "promedio": round(promedio, 2),
        "maximo": maximo,
        "minimo": minimo,
        "cantidad_pares": pares,
        "cantidad_impares": impares
    }


# Prueba
numeros = [4, 7, 2, 9, 12, 5, 8]
resultado = analizar_numeros(numeros)
print(resultado)