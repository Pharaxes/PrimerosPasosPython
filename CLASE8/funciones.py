# def saludo(nombre):
#     print(f"Hola {nombre}")
# 
# saludo("Martin")
# saludo("Alexander")
# print(saludo("Roberto")) #haciendo esto, imprime lo que retorna la funcion, en caso de no estar definido, "None"

# notas = [10, 8, 4, 7]
# # total_notas = sum(notas)
# # otra forma de hacer lo mismo
# total_notas = 0 
# 
# for nota in notas:
#     total_notas += nota
# 
# promedio = total_notas / len(notas)
# 
# print(f" Total: {total_notas}")
# print(f" Cantidad de notas: {len(notas)}")
# print(f" Promedio: {promedio}")
# 

#def promedio(items, precision = 2):
#    #return sum(notas) / len(notas) --> la forma facil
#    total_notas = 0
#    
#    for nota in items:
#        total_notas += nota
#
#    return round(total_notas / len(items), precision)
#
#print(f"Promedio de Martin: {promedio([8, 7, 9])}")
#print(f"Promedio de Alexander: {promedio([10, 5, 2])}")
#print(f"Promedio de Roberto: {promedio([8, 1, 2])}")

estudiantes = [
    {
      "nombre": "Martin",
      "notas": {
        "mate": {
          "parcial_1": 10,
          "parcial_2": 5,
          "parcial_3": 2,
          "nota_final": None
        },
        "literatura": {
          "parcial_1": 8,
          "parcial_2": 7,
          "parcial_3": 9,
          "nota_final": None
        }
      }
    },
    {
      "nombre": "Alexander",
      "notas": {
        "mate": {
          "parcial_1": 1,
          "parcial_2": 4,
          "parcial_3": 3,
          "nota_final": None
        },
        "literatura": {
          "parcial_1": 10,
          "parcial_2": 9,
          "parcial_3": 10,
          "nota_final": None
        }
      }
    },
]

# def suma(a, b):
#     resultado = a + b
#     return resultado
# 
# calculo = suma(5 , 6)
# print(calculo)

# *argas> permite pasar a una funcion un numero indeterminado/dinamico de argumentos posicionales. 
# args se usa por convencion, pero puede usarse cualquier nombre de argumento, lo importante es el asterisco
#def suma(*args):
#    print(args)
#    print(type(args))
#    resultado = 0
#    for numero in args:
#        resultado += numero
#    return resultado
#
#calculo = suma(5, 6, 9, 8)
#print(calculo)

# **kwargs: Permite pasar a una funcion un numero indeterminado/dinamico de argumentos nombrados (clave-valor | key-value)

#def ver_persona(**kwargs):
#    #print(kwargs)
#    #print(type(kwargs))
#
#    for key, value in kwargs.items():
#        print(f"Clave: {key} - Valor: {value}")


#{
#    nombre="Martin", 
#    edad=38, 
#    altura=1.75,
#    materias=["nada", "ninguna"]
#}

#ver_persona(nombre="Martin", edad=38, altura=1.75,materias=["nada", "ninguna"])


def funcion(a, b=1, *args, c, d=2, **kwargs):
    print("Parametros posicionales (positional / keyword)")
    print(f"a: {a}")
    print(f"b: {b}")

    print("Parametros posicionales indefinidos/indeterminado/dinamicos (*args)")
    print(f"args: {args}")

    print("Parametros nombrados (keyword only)")
    print(f"c: {c}")
    print(f"d: {d}")

    print("Parametros nombrados indefinidos/indeterminado/dinamicos (**kwargs)")
    print(f"kwargs: {kwargs}")

funcion(20,5, "otro posicional", "otro posicional2", "otro posicional3", c=30, d = True, algo="algo", algo2="algo2")