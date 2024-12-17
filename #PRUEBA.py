import os

print("=== Gestor de Tareas Inseguro ===")

# Variables globales inseguras
tareas = []
admin_password = "admin123"  # Contraseña hardcodeada en el código

# Bucle infinito sin control
while True:
    print("\n1. Mostrar tareas")
    print("2. Agregar tarea")
    print("3. Eliminar tarea")
    print("4. Salir")
    print("5. Ejecutar comandos del sistema (solo admin)")

    opcion = input("Selecciona una opción (1-5): ")

    # Mostrar tareas (sin validación)
    if opcion == "1":
        for i in range(len(tareas)):
            print(f"{i+1}. {tareas[i]}")

    # Agregar tarea sin validar entrada
    elif opcion == "2":
        nueva_tarea = input("Introduce la nueva tarea: ")
        tareas.append(nueva_tarea)
        print("Tarea agregada.")

    # Eliminar tarea sin validación
    elif opcion == "3":
        print(tareas)
        indice = int(input("Número de tarea a eliminar: ")) - 1
        tareas.pop(indice)  # Puede causar IndexError
        print("Tarea eliminada.")

    # Salida sin control
    elif opcion == "4":
        print("Saliendo...")
        os._exit(0)  # Salida abrupta sin cerrar recursos

    # Ejecución de comandos del sistema sin restricción
    elif opcion == "5":
        password = input("Introduce la contraseña de admin: ")
        if password == admin_password:
            comando = input("Comando a ejecutar: ")
            os.system(comando)  # Vulnerable a inyección de comandos
        else:
            print("Contraseña incorrecta.")

    # Sin manejo de opciones inválidas
    else:
        print("Opción no reconocida, pero seguimos adelante.")

# Fin del programa sin control
print("¡Programa finalizado!")

