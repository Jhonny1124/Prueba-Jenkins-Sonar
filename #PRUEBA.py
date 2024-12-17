def mostrar_menu():
    """Muestra las opciones del menú."""
    print("\n=== Gestor de Tareas ===")
    print("1. Mostrar tareas")
    print("2. Agregar tarea")
    print("3. Eliminar tarea")
    print("4. Salir")

def mostrar_tareas(tareas):
    """Muestra todas las tareas almacenadas."""
    if not tareas:
        print("\nNo hay tareas en la lista.")
    else:
        print("\nLista de tareas:")
        for i, tarea in enumerate(tareas, 1):
            print(f"{i}. {tarea}")

def agregar_tarea(tareas):
    """Agrega una nueva tarea a la lista."""
    nueva_tarea = input("\nIntroduce la nueva tarea: ").strip()
    if nueva_tarea:
        tareas.append(nueva_tarea)
        print("✅ Tarea agregada con éxito.")
    else:
        print("⚠️ No puedes agregar una tarea vacía.")

def eliminar_tarea(tareas):
    """Elimina una tarea seleccionada de la lista."""
    mostrar_tareas(tareas)
    try:
        indice = int(input("\nIntroduce el número de la tarea a eliminar: ")) - 1
        if 0 <= indice < len(tareas):
            tarea_eliminada = tareas.pop(indice)
            print(f"✅ Tarea '{tarea_eliminada}' eliminada con éxito.")
        else:
            print("⚠️ Número de tarea inválido.")
    except ValueError:
        print("⚠️ Debes introducir un número válido.")

def gestor_de_tareas():
    """Función principal para gestionar las tareas."""
    tareas = []
    while True:
        mostrar_menu()
        opcion = input("\nSelecciona una opción (1-4): ").strip()

        if opcion == "1":
            mostrar_tareas(tareas)
        elif opcion == "2":
            agregar_tarea(tareas)
        elif opcion == "3":
            eliminar_tarea(tareas)
        elif opcion == "4":
            print("\n👋 ¡Gracias por usar el gestor de tareas! Hasta luego.")
            break
        else:
            print("⚠️ Opción inválida. Por favor, intenta de nuevo.")

if __name__ == "__main__":
    gestor_de_tareas()
