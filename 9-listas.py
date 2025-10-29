print("#### LISTAS ####")

#Se define entre corchetes, son ordenadas(elementos tienen indice)
#Son mutables (agregar, modificar y eliminar)

#           0     1    2    3    --indice
lista = ["info", 10, 1.75, True] 
print(f"Valor: {lista}, tipo: {type(lista)}")

#                     -1
#          0  1  2  3  4
numeros = [1, 2, 3, 4, 5, 'info']
print(f"Primer elemento: {numeros[0]}")
print(f"Ultimo elemento: {numeros[-1]}")

#slicing
print(f"Primeros tres elemento: {numeros[:3]}")
print(f"Ultimos dos elemento: {numeros[-2:]}")
print(f"Elementos del medio: {numeros[1:-1]}")

print(f"Longitud de la lista: {len(numeros)}")
print(f"Veces que aparece el 'info': {numeros.count('info')}")

numeros[0] = True
print(f"Despues de modificar: {numeros}")

numeros.append("algo")
print(f"Despues de agregar: {numeros}")

#si no se le pasa indice, se elimina el ultimo componente
numeros.pop()
print(f"Despues de eliminar: {numeros}")

numeros.remove("info")
print(f"Despues de eliminar: {numeros}")

matriz = [
#    0  1  2
    [1, 2, 3], # 0
    [4, 5, 6], # 1
    [7, 8, 9], # 2
]
print(f"Elemento en [1][1] {matriz[1][1]}")
