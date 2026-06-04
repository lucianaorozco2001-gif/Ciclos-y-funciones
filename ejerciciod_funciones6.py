def calcular_propina(total, porcentaje=15):
    """Calcula la propina y el total a pagar"""
    propina = total * (porcentaje / 100)
    total_con_propina = total + propina
    return propina, total_con_propina


def main():
    print("=== Calculadora de Propinas ===")
    total = float(input("Ingrese el total de la cuenta: $"))
    porcentaje = float(input("Ingrese el porcentaje de propina (por defecto 15): ") or 15)
    
    propina, total_final = calcular_propina(total, porcentaje)
    
    print(f"\nPropina ({porcentaje}%): ${propina:.2f}")
    print(f"Total a pagar: ${total_final:.2f}")


main()