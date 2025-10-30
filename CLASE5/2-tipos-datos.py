print("#### DATOS PRIMITIVOS ####")

nombre = "Martin"
print(f"Valor: {nombre}, tipo: {type(nombre)}")

edad = 38
print(f"Valor: {edad}, tipo: {type(edad)}")

altura = 1.75
print(f"Valor: {altura}, tipo: {type(altura)}")

es_estudiante = False
print(f"Valor: {es_estudiante}, tipo: {type(es_estudiante)}")

complejo = complex(2, 3)
print(f"Valor: {complejo}, tipo: {type(complejo)}")

valor = None
print(f"Valor: {valor}, tipo: {type(valor)}")

nan = float("nan")
print(f"Valor: {nan}, tipo: {type(nan)}")

print("#### ESTRUCTURAS DE DATOS ####")

lista = ["manzana", "naranja", "mandarina", True, 15 ]
#los componentes de una lista se escriben entre corchetes separados por comas
print(f"Valor: {lista}, tipo: {type(lista)}")

tupla = ("manzana", "naranja", "mandarina")
#los componentes de una tupla se escriben entre parentesis separados por coma. Al contrario de las listas, una vez creada no se puede modificar los componentes
print(f"Valor: {tupla}, tipo: {type(tupla)}")

set_mio = {"manzana", "naranja", "mandarina"}
#los componentes de un set se escriben entre llaves separados por comas
print(f"Valor: {set_mio}, tipo: {type(set_mio)}")

diccionario = {"nombre" : "Martin", "edad" : 35, "altura" : 1.75}
#los componentes de un diccionario se escriben entre llaves separados por comas. Cada componente tiene tipo y valor separados por dos puntos
print(f"Valor: {diccionario}, tipo: {type(diccionario)}")


