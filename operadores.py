#operadores aritmeticos
print(3+3)
print(4-5)
print(2*2)
print(8/2)
print(85 % 10)
print(11 // 2)
print(2**3)

#operadores en cadenas de texto
print("hola"+"mundo") #concatenacion
print("hola"*3) #repeticion
print("hola"+"mundo"*3) 

#operadores de compracion
print("hola"=="HOLA") #igual que
print("hola"!="HOLA") #distinto que
print(3>11) #mayor que
print(11>=10) #mayor igual que
print(10<=10) #menor igual que

#operadores de existencia
print ("ola" in "Hola") #de existencia
print("ola" not in "hola") #de inexitencia

#operadores booleanos
print(True or False) #compuerta or
print (True and False) #compuerta not

#operadores de asignacion 
x=1 #operador de asignasion estandar
print(x) 
x +=2 #operador de asignasion suma
print(x)
x *=3 #operador de asignasion multiplicacion
print(x)
x %=4 #operador de asignasion modulo 
print(x)

#las operaciones aritmeticas se resuelven segun su orden jerarquico 
x = 2+3-1*5/2**4
print(x)
