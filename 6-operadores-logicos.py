print("#### OPERADORES LOGICOS ####")

a = 10
b = 3
c = 20

print("\n --- OPERADOR AND ---")
#           True  y   True
resultado = 10 > 3 and 10 < 20
print(f"10 > 3 and 10 < 20: {resultado}")

print("\n --- OPERADOR OR ---")
#           True  o  False
resultado = 10 > 3 or 10 < 5
print(f"10 > 3 or 10 < 5: {resultado}")

print("\n --- OPERADOR NOT ---")
resultado = 10 > 3 
print(f"10 > 3: {resultado}")
resultado = not 10 > 3 
print(f"not 10 > 3: {resultado}")

esta_autenticado = False
if not esta_autenticado:
    print("Por favor, inicia sesion")