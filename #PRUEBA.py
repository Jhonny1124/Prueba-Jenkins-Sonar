print("\n=== Gestor de Tareas ===")
tareas = []
while True:
    # Mostrar menú
    print("\n1. Mostrar tareas")
    print("2. Agregar tarea")
    print("3. Eliminar tarea")
    print("4. Salir")

    opcion = input("\nSelecciona una opción (1-4): ").strip()

    # Mostrar tareas
    if opcion == "1":
        if not tareas:
            print("\nNo hay tareas en la lista.")
        else:
            print("\nLista de tareas:")
            i = 1
            for tarea in tareas:
                print(f"{i}. {tarea}")
                i += 1

    # Agregar una tarea
    elif opcion == "2":
        nueva_tarea = input("\nIntroduce la nueva tarea: ").strip()
        if nueva_tarea:
            tareas.append(nueva_tarea)
            print("✅ Tarea agregada con éxito.")
        else:
            print("⚠️ No puedes agregar una tarea vacía.")

    # Eliminar una tarea
    elif opcion == "3":
        if not tareas:
            print("\nNo hay tareas para eliminar.")
        else:
            print("\nLista de tareas:")
            i = 1
            for tarea in tareas:
                print(f"{i}. {tarea}")
                i += 1

            try:
                indice = int(input("\nIntroduce el número de la tarea a eliminar: ")) - 1
                if 0 <= indice < len(tareas):
                    tarea_eliminada = tareas.pop(indice)
                    print(f"✅ Tarea '{tarea_eliminada}' eliminada con éxito.")
                else:
                    print("⚠️ Número de tarea inválido.")
            except ValueError:
                print("⚠️ Debes introducir un número válido.")

    # Salir del programa
    elif opcion == "4":
        print("\n👋 ¡Gracias por usar el gestor de tareas! Hasta luego.")
        break

    # Opción no válida
    else:
        print("⚠️ Opción inválida. Por favor, intenta de nuevo.")

