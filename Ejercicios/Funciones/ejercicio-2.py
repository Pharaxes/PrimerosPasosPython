# 2- Sumar todos los números 
# Definí una función sumar_todos() utilizando args que reciba una cantidad indefinida de 
# números y devuelva la suma total (Acá podemos usar la función integrada de python sum)

def sumar_todos(*args):
    """
    Recibe cualquier cantidad de numeros, y retorna la suma
    """
    return sum(args)
    

print(sumar_todos(20,5,6,8,95))


numeros = []
while True:
    try:
        numero = int(input("Ingrese un numero: "))
        numeros.append(numero)
    except ValueError:
        print("Eso no es un número válido. Intente de nuevo.")
        continue

    respuesta = input("desea continuar? (S/N)" ).upper()
    if respuesta == "N":
        break

print(f"La suma de los numeros ingresados es: {sumar_todos(*numeros)}")