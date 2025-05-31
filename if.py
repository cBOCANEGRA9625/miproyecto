# animal = input("dime un animal")
# if animal == "perro":
#      print ("-guau")
# print ("conozco pocos animales")

# num = int(input("ingrese un entero"))
# if num<0:
#      num = -num
# print("su valor absoluto es: ", num)

# servicio = int (input ("Que kilometraje tiene tu carro? "))

# if servicio < 10000:
#     print ("servicio de cambio de aceite")
# elif servicio > 40000:
#     print ("servicio aceite y cambio de balatas")

# Salir = input ("¿Saldras el dia de hoy?" )

# edad = false

# if entrada .isnumeric() :
#      edad = int(entrada)
# else :
#      print ("Dato incorrecto, es necesario un numero")
#      exit ()

# if edad <= 0:
#      print ("Eres demaciado joven... Imposible. Trata de nuevo")
# elif edad > 100 :
#      print ("Alguien tan viejo, no deberias fumar. TRata de nuevo")
# elif edad < 18 :
#      print ("alguien menor de edad no deberia fumar...")
# else :
#      print ("eres mayor de edad, aqui esta tu cigarro")

Salir = input("¿Saldrás de casa hoy?: ").lower() #.lower es para aceptar cualquier valor

if Salir == "si":
    Salir = input("¿Apagaste todas las luces?: ").lower()
    if Salir != "si":
        print("Entonces apaga todas las luces")
    
    Salir = input("¿Las mascotas tienen agua y alimento?: ").lower()
    if Salir != "si":
        print("Entonces pon agua y comida a las mascotas!!!")
    
    Salir = input("¿Llevas tu cartera?: ").lower()
    if Salir != "si":
        print("Entonces lleva tu cartera")
    
    Salir = input("¿La puerta tiene llave?: ").lower()
    if Salir == "si":
        print("Perfecto, tienes todo listo para salir")
    else:
        print("Entonces ponle llave a la puerta")
else:
    print("No salir de casa ayuda a ahorrar dinero")



            
            
            