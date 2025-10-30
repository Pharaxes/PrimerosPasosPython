print("#### DICCIONARIOS ####")
# Se definen entre llaves { }
# Estan compuestos con clave-valor (key-value)
# No son ordenados, no poseen indice, sino que se acceden mediante su clave

#nombre = input("Ingresa el nombre: ")
#edad = int(input("Ingresa la edad: "))
#altura = float(input("Ingresa la altura: "))

estudiante = {
    "nombre" : "Ana",
    "edad" : 22,
    "altura" : 1.65,
    "cursos" : {
        "programacion" : {
            "profesor" : "Romero" ,
            "horario" : [
                "8:00", 
                "10:00"
                ] ,
        },
        "disenio" : {
            "profesor" : "Elias" ,
            "horario" : [
                "10:00", 
                "12:00"
                ] ,
        }
    }
}

print(f"Valor: {estudiante}, tipo: {type(estudiante)}")
print(f"El nombre es: {estudiante ["nombre"]}")
print(f"Los cursos en los que esta son: {estudiante ["cursos"]}")
print(f"El horario del curso de disenio es: {estudiante ["cursos"]["disenio"]["horario"]}")
print(f"El horario de inicio del curso de disenio es: {estudiante ["cursos"]["disenio"]["horario"][0]}")
print(f"El horario de final del curso de disenio es: {estudiante ["cursos"]["disenio"]["horario"][1]}")
print(f"El profesor del curso de disenio es: {estudiante ["cursos"]["disenio"]["profesor"]}")

print("#### METODOS ####")
print(f"Claves del diccionario: {estudiante.keys()}")
print(f"Claves del diccionario: {list(estudiante.keys())}")
print(f"Valores del diccionario: {list(estudiante.values())}")
print(f"Items del diccionario: {list(estudiante.items())}")
