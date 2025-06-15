agenda = {
    "Ilse": {"Profesion": "Astronoma", "telefono": "555-111", "Ciudad": "Toronto" },
    "Luis": {"Profesion": "Ingeniero", "telefono": "555-222", "Ciudad": "Dallas" },
    "Julio": {"Profesion": "Sistemas", "telefono": "555-333", "Ciudad": "Santiago de Chile" },
    "Cesar": {"Profesion": "Ing. en Mantenimiento,", "telefono": "555-444", "Ciudad": "Apodaca" }
}
nom = input("Ingresa el nombre de la persona para ver su profesión: ")
if nom in agenda:
   profresion = agenda [nom]["Profesion"]
   telefono = agenda [nom]["telefono"]
   print = (f"{nom} quiere ser {profresion} y su telefono es {telefono}")
else:
   print ("Esta persona no esta en la agenda")