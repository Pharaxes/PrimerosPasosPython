print("#### OPERADORES DE COMPARACION ####")

a = 10
b = 3
print(f"a == b: {a == b}")
print(f"a is b: {a is b}")

x = "Hola"
y = "Hola"
print(f"x == y: {x == y}")
print(f"x is y: {x is y}")

lista_uno = [10, 20, 30]
lista_dos = [10, 20, 30]
print(f"lista_uno == lista_dos: {lista_uno == lista_dos}")
print(f"lista_uno is lista_dos: {lista_uno is lista_dos}")
#en caso de listas, el comparador "is" no optimiza al asignar el mismo espacio a memoria a las listas, por mas que sean iguales, como si pasa en variables

resultado = a > b
print(f"a > b: {resultado}")

resultado = a < b
print(f"a < b: {resultado}")

resultado = a >= b
print(f"a >= b: {resultado}")

resultado = a <= b
print(f"a <= b: {resultado}")

resultado = a != b
print(f"a != b: {resultado}")