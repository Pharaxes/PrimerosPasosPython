# while 1 == 1: bucle infinito, e lo mismo que while True
# Para detener un bucle infinito, se puede hacer con Ctrl C, haciendo clic en la terminal

#bandera = True
estudiantes = []

while True:
    
    respuesta = input("Desea continuar? (S/N)")
    if respuesta == "N":
        print("chau")
        break
        #bandera = False
    elif respuesta == "S":
        print("Continuamos")

        nombre = input("Ingresa el nombre del estudiante: ")
        edad = input("Ingresa la edad del estudiante: ")

        estudiantes.append({
            "nombre" : nombre,
            "edad" : edad
        })


        
    elif respuesta == "X":
        print("Presionaste X")
        continue
    else:
        print("Valor invalido")

print(f"Estudiantes registrados: {estudiantes}")