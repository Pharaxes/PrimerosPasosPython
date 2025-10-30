print("#### STRINGS INTRO A F-STRINGS ####")

nombre="Martin"
apellido="Romero"

mensaje=f"Hola {nombre}, {apellido}"
print(mensaje)

mensaje_dos="Hola {}, {}".format(nombre, apellido)
print(mensaje_dos)

num_1=5
num_2=10

mensaje_tres=f"La suma de {num_1} + {num_2} es igual a {num_1 + num_2}"
print(mensaje_tres)

mensaje_cuatro=f"La suma de {num_1} + {num_2}:\n {num_1 + num_2}"
print(mensaje_cuatro)

cadena="Hola info "
cadena_repetida=cadena*3
print(cadena_repetida)

#LONGITUD
texto="cinco"
longitud=len(texto)
print(type(texto))
print(longitud)

#SLICE
texto_dos = "Hola Info 🚀"
#el tercer numero es el intervalo del slice
subcadena = texto_dos[5:9:2]
print(subcadena)

#INVERTIR
cadena_invertida = texto_dos[::-1]
print(cadena_invertida)

#MAYUSCULA
cadena_mayusculas = texto_dos.upper()
print(cadena_mayusculas)

#MINUSCULA
cadena_minusculas = texto_dos.lower()
print(cadena_minusculas)

#CAPITALICE (la primera en mayuscula, pero solo de la primer palabra)
nombre_dos = "martin romero"
cadena_capitalizada = nombre_dos.capitalize()
print(cadena_capitalizada)

cadena_tabulada = "\tHola\tInfo"
print(cadena_tabulada)

comillas_escapadas = "en el 'caso' tal cosa"
print(comillas_escapadas)
#para poder escribir comillas dobles, hasy que usar un escape, para que no lo tome como el cierre del string
comillas_escapadas = "en el \"caso\" tal cosa"
print(comillas_escapadas)