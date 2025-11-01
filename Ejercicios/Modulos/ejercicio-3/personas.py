# 3- Info de las personas 
# Crear un módulo llamado personas.py que contenga funciones para:
# 1- mostrar_info(nombre, edad, ciudad) e imprima la información de una persona de forma legible
# 2- mayor-de-edad(edad) devuelve True si la persona es mayor de 18 años, False si no.


def mostrar_info(nombre, edad, ciudad):
    print(f"\nNombre: {nombre}")
    print(f"Edad: {edad}")
    print(f"Ciudad: {ciudad}")

def mayor_de_edad(edad):
    if edad >= 18:
        print("\nEs mayor de edad")
    else:
        print("\nNo es mayor de edad")