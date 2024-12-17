#PRUEBA
def sumar_numeros():
    """
    Solicita al usuario dos números y devuelve su suma.
    Realiza validación de entrada para evitar errores.
    """
    try:
        # Solicitar números al usuario con validación
        numero1 = float(input("Introduce el primer número: "))
        numero2 = float(input("Introduce el segundo número: "))

        # Realizar la suma
        resultado = numero1 + numero2

        # Mostrar el resultado
        print(f"La suma de {numero1} y {numero2} es: {resultado}")
    except ValueError:
        # Manejar entradas no válidas
        print("Error: Solo puedes introducir números.")

if __name__ == "__main__":
    print("=== Calculadora de Suma ===")
    sumar_numeros()