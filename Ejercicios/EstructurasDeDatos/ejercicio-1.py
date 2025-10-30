# Ejercicio 1: Gestión de una lista de compras
# Crea una lista vacía llamada lista_compras
# Luego:
# 1- Agregá 3 productos usando .append()
# 2- Mostrá cuántos productos hay con len()
# 3- Eliminá el último producto con .pop()
# 4- Mostrá la lista actualizada
# El objetivo es aprender .append(), .pop() y .len()

lista_compras = []
lista_compras.append("lavandina")
lista_compras.append("javon")
lista_compras.append("detergente")

print(f"Hay comprar: {lista_compras}")
print(f"Hay comprar {len(lista_compras)} productos")

lista_compras.pop()

print(f"Hay comprar: {lista_compras}")
print(f"Hay comprar {len(lista_compras)} productos")
