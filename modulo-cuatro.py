NumeroHuevos=24

#opcion1
print("tengo "+str(NumeroHuevos)+"huevos")

#opcion2
print("tengo %s huevos: " %(NumeroHuevos))

#errores de logica
lado=int(input("ingresa la medida del lado del cuadrado: "))
superficie= lado * lado
print("el area es: " + str(superficie))
################################################

#ejercico de la semana
nombre = input("Introduce tu nombre: ")
apellido = input("Introduce tu apellido: ")
edad = input("Introduce tu edad: ")
correo = input("Introduce tu correo electronico")
telefono = input("Introduce tu telefono: ")

print ("Nombre: " + nombre)
print ("Apellido" + apellido)
print ("Tengo " + str(edad) + "años")
print ("Mi correo es: " + correo)
print ("Telefono: " + telefono)
