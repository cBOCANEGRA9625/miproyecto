#programa creado para calcular indice de masa corporal.

#definicion de variables. Se crearan 5 variables 
variable1 = input("Nombre completo con apellido paterno y materno: ")
variable2 = input("Edad: ")
variable3 = float(input("peso en kilogramos: "))
variable4 = float(input("estatura en metros: "))
variable5 = float(variable4 * variable4)
#variable6 = float (variable3 / variable5)
print (variable1)
print("EDAD " + variable2 + " años")
print (f"su indice de masa corporal (IMC) es: {variable3 / variable5}")
