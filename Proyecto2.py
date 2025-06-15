# Solicitar una palabra válida (entre 4 y 8 caracteres)
while True:
    palabra = input("Ingresa una palabra (entre 4 y 8 letras): ")  # Solicita la palabra al usuario
    longitud = len(palabra)  # Calcula la longitud de la palabra

    if 4 <= longitud <= 8:  # Verifica si la longitud está entre 4 y 8
        print("✅ Palabra correcta.")  # Mensaje si la palabra es válida
        break  # Sale del ciclo si la palabra es válida
    elif longitud < 4:  # Si tiene menos de 4 letras
        print(f"⚠️ Hacen falta letras. Solo tiene {longitud} letras.")  # Mensaje de advertencia
    else:  # Si tiene más de 8 letras
        print(f"⚠️ Sobran letras. Tiene {longitud} letras.")  # Mensaje de advertencia

# Solicitar coordenadas válidas (ni X ni Y pueden ser cero)
while True:
    try:
        x = int(input("Ingresa la coordenada X (≠ 0): "))  # Solicita valor entero para X
        y = int(input("Ingresa la coordenada Y (≠ 0): "))  # Solicita valor entero para Y

        if x == 0 or y == 0:  # Verifica si alguno es cero
            print("⚠️ X e Y no pueden ser cero. Intenta de nuevo.")  # Mensaje de error
        else:
            break  # Sale del ciclo si ambos valores son válidos
    except ValueError:  # Captura errores si el usuario no ingresa un número entero
        print("⚠️ Debes ingresar números enteros. Intenta de nuevo.")  # Mensaje de error

# Determinar el cuadrante en el que se encuentra el punto
if x > 0 and y > 0:  # Si X e Y son positivos
    print("📍 El punto se encuentra en el cuadrante I.")  # Resultado: Cuadrante I
elif x < 0 and y > 0:  # Si X es negativo y Y positivo
    print("📍 El punto se encuentra en el cuadrante II.")  # Resultado: Cuadrante II
elif x < 0 and y < 0:  # Si ambos son negativos
    print("📍 El punto se encuentra en el cuadrante III.")  # Resultado: Cuadrante III
elif x > 0 and y < 0:  # Si X es positivo y Y negativo
    print("📍 El punto se encuentra en el cuadrante IV.")  # Resultado: Cuadrante IV