tareas = []

def mostrar_menu():
    print("\n" + "="*40)
    print("  GESTOR DE TAREAS  ".center(40))
    print("="*40)
    print("1. Agregar tarea")
    print("2. Ver todas las tareas")
    print("3. Marcar como completada")
    print("4. Eliminar tarea")
    print("5. Buscar tarea")
    print("6. Estadísticas")
    print("7. Salir")
    print("="*40)


def agregar_tarea(lista_tareas):
    descripcion = input("\nDescripción de la tarea: ").strip()
    
    print("Prioridad:")
    print("1. Alta")
    print("2. Media")
    print("3. Baja")
    opcion = input("Elige (1-3): ")
    
    prioridades = {"1": "alta", "2": "media", "3": "baja"}
    prioridad = prioridades.get(opcion, "media")
    
    tarea = {
        "descripcion": descripcion,
        "completada": False,
        "prioridad": prioridad
    }
    
    lista_tareas.append(tarea)
    print(f"✅ Tarea agregada con prioridad {prioridad}")


def mostrar_tareas(lista_tareas):
    if not lista_tareas:
        print("\nNo hay tareas registradas")
        return
    
    print("\n" + "="*60)
    print("  LISTA DE TAREAS  ".center(60))
    print("="*60)
    
    for i, tarea in enumerate(lista_tareas, 1):
        estado = "✅ Completada" if tarea["completada"] else "⏳ Pendiente"
        prioridad = tarea["prioridad"].upper()
        print(f"{i}. {estado} [{prioridad}] {tarea['descripcion']}")
    print("="*60)


def marcar_completada(lista_tareas):
    mostrar_tareas(lista_tareas)
    if not lista_tareas:
        return
    try:
        num = int(input("\n¿Qué tarea completaste? (número): "))
        if 1 <= num <= len(lista_tareas):
            lista_tareas[num-1]["completada"] = True
            print("¡Tarea marcada como completada!")
        else:
            print("Número inválido")
    except ValueError:
        print("Debes ingresar un número")


def eliminar_tarea(lista_tareas):
    mostrar_tareas(lista_tareas)
    if not lista_tareas:
        return
    try:
        num = int(input("\n¿Qué tarea quieres eliminar? (número): "))
        if 1 <= num <= len(lista_tareas):
            eliminada = lista_tareas.pop(num-1)
            print(f"Tarea eliminada: {eliminada['descripcion']}")
        else:
            print("Número inválido")
    except ValueError:
        print("Debes ingresar un número")


def buscar_tarea(lista_tareas):
    palabra = input("\nPalabra clave a buscar: ").lower()
    encontradas = [(i+1, t) for i, t in enumerate(lista_tareas) if palabra in t["descripcion"].lower()]
    
    if not encontradas:
        print("No se encontraron tareas")
    else:
        print(f"\nSe encontraron {len(encontradas)} tarea(s):")
        for num, tarea in encontradas:
            estado = "✅" if tarea["completada"] else "⏳"
            print(f"{num}. {estado} {tarea['descripcion']}")


def mostrar_estadisticas(lista_tareas):
    total = len(lista_tareas)
    if total == 0:
        print("\nNo hay tareas")
        return
    
    completadas = sum(1 for t in lista_tareas if t["completada"])
    alta = sum(1 for t in lista_tareas if t["prioridad"] == "alta")
    media = sum(1 for t in lista_tareas if t["prioridad"] == "media")
    baja = sum(1 for t in lista_tareas if t["prioridad"] == "baja")
    porcentaje = (completadas / total) * 100
    
    print("\n" + "="*40)
    print("  ESTADÍSTICAS  ".center(40))
    print("="*40)
    print(f"Total de tareas:     {total}")
    print(f"Completadas:         {completadas}")
    print(f"Progreso:            {porcentaje:.1f}%")
    print(f"\nPor prioridad:")
    print(f"  Alta:   {alta}")
    print(f"  Media:  {media}")
    print(f"  Baja:   {baja}")
    print("="*40)


def main():
    while True:
        mostrar_menu()
        opcion = input("\nElige una opción: ")
        
        if opcion == "1":
            agregar_tarea(tareas)
        elif opcion == "2":
            mostrar_tareas(tareas)
        elif opcion == "3":
            marcar_completada(tareas)
        elif opcion == "4":
            eliminar_tarea(tareas)
        elif opcion == "5":
            buscar_tarea(tareas)
        elif opcion == "6":
            mostrar_estadisticas(tareas)
        elif opcion == "7":
            print("\n¡Hasta luego! Sigue siendo productivo ✨")
            break
        else:
            print("Opción inválida")
        
        input("\nPresiona ENTER para continuar...")


if __name__ == "__main__":
    main()