pacientes = ["Ana Garcia", "Luis Martinez", "Camila Soto", "Pedro Rojas"]

nombre = input("Ingrese nombre del paciente: ")

if nombre in pacientes:

    lugar = pacientes.index(nombre)

    print("Paciente registrado")
    print("Posicion en la lista:", lugar)

else:

    print("El paciente no existe en el registro")