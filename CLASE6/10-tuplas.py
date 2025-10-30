print("#### TUPLAS ####")

#Se define entre parentesis, son ordenadas(elementos tienen indice)
#Son inmutables (no se puede agregar, modificar y eliminar)
tupla = ("manzanas", "naranjas", "frutillas")
print(f"Valor: {tupla}, tipo: {type(tupla)}")

print(f"Primer elemento: {tupla[0]}")
print(f"Ultimo elemento: {tupla[-1]}")

print(f"Longitud de la lista: {len(tupla)}")
print(f"Veces que aparece 'frutillas': {tupla.count('frutillas')}")
print(f"El indice de 'naranjas': {tupla.index("naranjas")}")

a, b, c = tupla
print(f"Desempaquetado a={a}, b={b}, c={c}")

primer_elem, *resto = tupla
print(f"Desempaquetado Primero={primer_elem}, Resto={resto}")
