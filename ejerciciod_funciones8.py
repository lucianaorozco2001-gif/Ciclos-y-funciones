def validar_contraseña(contraseña):
    if len(contraseña) < 8:
        return False
    if not any(c.isupper() for c in contraseña):
        return False
    if not any(c.isdigit() for c in contraseña):
        return False
    return True


def solicitar_contraseña():
    while True:
        pwd = input("Ingrese una contraseña: ")
        if validar_contraseña(pwd):
            print("✅ Contraseña válida!")
            return pwd
        else:
            print("❌ Contraseña inválida. Debe tener al menos 8 caracteres, 1 mayúscula y 1 número.")


# Prueba
contraseña_valida = solicitar_contraseña()
print(f"Contraseña aceptada: {contraseña_valida}")