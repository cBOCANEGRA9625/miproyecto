d1 = {
    "Ilse": "Fisica",
    "Luis": "Ingeniero",
    "Julio": "sistemas",
    "Cesar": "Ing. en Mantenimiento"
}
nom = input("Ingresa el nombre de la persona para ver su profesión: ")
if nom in d1:
    print(f"La profesión de {nom} es: {d1[nom]}")
else:
    print(f"Lo siento, '{nom}' no se encontró en el diccionario.")