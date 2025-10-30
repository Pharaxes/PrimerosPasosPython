print("#### CONJUNTOS O SETS ####")
# Se definen ent5re llaves {}
# No permiten elementos ducplicados
# No son ordenados (no se puede acceder a elementos mediante indice)
# Son mutables (Se pueden modificar, agregar y eliminar elementos).

colores = {"rojo", "verde", "azul"}
print(f"Valor: {colores}, tipo: {type(colores)}")

colores.add("amarillo")
print(f"Conjunto despues del add: {colores}")

colores.add("amarillo")
print(f"Conjunto despues del add: {colores}")

colores.remove("verde")
print(f"Conjunto despues del remove: {colores}")

colores.add("naranja")
print(f"Conjunto despues del add: {colores}")

colores.discard("naranja")
print(f"Conjunto despues del remove: {colores}") #Discrad revisa si el elemento esta, y entonces lo remueve. Si no existe, no tira error, al contrario de Remove

colores.discard("violeta")
print(f"Conjunto despues del remove: {colores}")

conjunto = {"hola info", True, 42, (1, 2)} #puede contener cualquier tipo de dato, o estructura de dato

