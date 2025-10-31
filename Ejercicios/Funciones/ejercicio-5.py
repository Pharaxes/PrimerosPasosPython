# 5- Registro flexible de usuarios 
# Creá una función registrar_usuario() que reciba_
# *args con los intereses del usuario, por ejemplo (Música, Programación, Videojuegos, etc)
# **kwargs con su información básica (nombre, edad, etc.)
# Y que devuelva un resumen legible.

def registrar_usuario(*args, **kwargs):
    print("\n DATOS PERSONALES \n")
    for clave, valor in kwargs.items():
        print(f" - {clave.capitalize()} : {valor}")
    
    print("\n INTERESES \n")
    for interes in args:
        print(f" - {interes.capitalize()}")
    


    
registrar_usuario("motos", "rol", nombre = "Martin", edad = 38)