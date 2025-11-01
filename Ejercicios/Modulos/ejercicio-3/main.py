# 3- Info de las personas 
# Crear un módulo llamado personas.py que contenga funciones para:
# 1- mostrar_info(nombre, edad, ciudad) e imprima la información de una persona de forma legible
# 2- mayor-de-edad(edad) devuelve True si la persona es mayor de 18 años, False si no.
# 
# Luego, crear un archivo main.py que importe el módulo, pida datos al usuario y muestre la
# información junto con si es mayor de edad o no

import personas
print("\n BIENVENIDO\n")
nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
ciudad = input("Ingrese su ciudad de origen: ")

personas.mostrar_info(nombre, edad, ciudad)
personas.mayor_de_edad(edad)

