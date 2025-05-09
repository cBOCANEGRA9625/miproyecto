nombre = input("¿como te llamas?")
print("hola " + nombre)

edad = input("cuantos años tienes? ")
print(type(edad))
print(f"{nombre} tiene {edad} años")

#programa que pide 2 numeros al usuario y los suma
numero1 = int(input("introduce un numero:"))
numero2 = int(input("introduce un numero:"))
numero3 = int(numero1 ** numero2)
print("Dos a la potencia 3 es:", numero3) #Porque las 2 lineas dan el mismo resultado?
print(f"Dos a la potencia 3 es: {numero3}") #Porque las 2 lineas dan el mismo resultado?
