# 4- Mostrar información de una persona con **Kwargs 
# Creá una función mostrar_info() que reciba datos como nombre, edad, ciudad, etc, y los
# muestre con un formato legible.

def mostrar_info(**kwargs):
    for clave, valor in kwargs.items():
        print(f"{clave.capitalize()} : {valor}")


info_persona = {}
while True:

    dato = input("Que informacion desea ingresar? : ").capitalize()
    valor = input("Ingrese la informacion : ").capitalize()
    
    info_persona[dato] = valor
    
    respuesta = input("desea continuar? (S/N): " ).upper()
   
    while respuesta not in ("S", "N"):
        print("Por favor ingrese solo 'S' o 'N'.")
        respuesta = input("¿Desea continuar? (S/N): ").upper()
    
    if respuesta == "N":
        break

print(f"\nInfo: {info_persona}\n")

mostrar_info(**info_persona)


# print("Informacion de la persona")
# mostrar_info(nombre = "Martin", edad = 38, ciudad = "Resistencia")