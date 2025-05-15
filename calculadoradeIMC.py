#programa creado para calcular indice de masa corporal.

#definicion de variables. Se crearan 6 variables 
variable1 = ""
while variable1 == "":
    variable1 = input("Nombre (Solo nombre, apellidos no): ")
variable6 = ""
while variable6 == "":
    variable6 = input("Apellido paterno y apellido manterno: ")
variable2 = ""
while variable2 == "":
   variable2 = input("Edad: ")

#variable3 = 0 Este codigo puede fallar con cualquier cosa que no se sea un numero o valores negativos
#while variable3 == 0: Este codigo da proble,a porque, si acepta el 0, esa operacion no se podra realizar
    #variable3 = float(input("peso en kilogramos: ")). al no poder variable3 entre variable 5 da error

while True:
    try:
        variable3 = float(input("Peso en kilogramos: "))
        if variable3 > 0:
            break
        else:
            print("Por favor, escribe un número mayor que 0.")
    except ValueError:
        print("Eso no es un número válido. Intenta de nuevo.")

#variable4 = "" codigo solo valido para string
#while variable4 == "": codigo solo valido para string
    #variable4 = float(input("estatura en metros: ")) codigo solo valido para string

while True:
    try:
        variable4 = float(input("Estatura en metros: "))
        if variable4 > 0:
            break
        else:
            print("Por favor, escribe un número mayor que 0.")
    except ValueError:
        print("Eso no es un número válido. Intenta de nuevo.")

variable5 = float(variable4 * variable4)
#variable6 = float (variable3 / variable5) Usando cadena formateada no ahorramos esta linea
print (variable1 + variable6)
print("EDAD " + variable2 + " años")
print (f"su indice de masa corporal (IMC) es: {variable3 / variable5}")
