# 3- Mutiplicar todos los números 
# Escribí una función multiplicar() utilizando args, que reciba varios números y devuelva el
# resultado de multiplicarlos todos.

def multiplicar(*args):
    '''
    Recibe cualquier cantidad de numeros y retorna la multiplicacion
    Si no se pasan argumentos, devuelve 1
    '''
    resultado = 1
    for n in args: 
        resultado *= n
    return resultado

print(multiplicar(5, 5, 2))

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

print(f"La suma de los numeros ingresados es: {multiplicar(*numeros)}")