#sistema de triage en servicio de urgencias
pacientes = []
while True:
    nombre = input ("ingresar nombre de paciente:")
    edad = int(input("ingresar edad del paciente:"))
    sintomas = input("ingresar sintomas del paciente:")
    paciente = {"nombre": nombre, "edad": edad, "sintomas": sintomas}
    pacientes.append(paciente) 
    continuar = input ("¿desea agregar otro paciente? (si/no):")
    if continuar != "si":
        break 
    print("lista de pacientes en triage:")
    for paciente in pacientes:
        print(f"Nombre: {paciente['nombre']}, Edad: {paciente['edad']}, Sintomas: {paciente['sintomas']}")
        