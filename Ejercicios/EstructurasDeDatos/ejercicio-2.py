# Ejercicio 2: Contar apariciones
# Dada la lista:
# colores = ["rojo", "azul", "verde", "rojo", "azul", "rojo"]
# 1- Mostrá cuántas veces aparece “rojo” usando .count().
# 2- Reemplazá el primer “verde” por “amarillo”
# 3- Mostrá la lista final
# El objetivo es usar el método .count(), acceso por índice, asignación de valor. 

colores = ["rojo", "azul", "verde", "rojo", "azul", "rojo"]

print(f"Lista de colores: {colores}")
print(f"\"rojo\" aparece {colores.count("rojo")} veces en la lista")

pos_verde = colores.index("verde")
colores[pos_verde] = "amarillo"
print(f"Lista de colores: {colores}")
