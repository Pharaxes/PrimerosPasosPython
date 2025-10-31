# 1-Sistema de calificaciones de estudiantes
# Creá un programa que guarde las notas de varios estudiantes en un diccionario,
# Luego, crea funciones para:
# A- Agregar estudiante con sus notas
# B- Calcular el promedio de un estudiante
# C- Mostrar los estudiantes aprobados (promedio >=6)




estudiantes = {}

def agregar_estudiante(nombre,  notas):
    '''
    nombre: str --> nombre del estudiante
    notas: list --> lista de enteros que representa las ntas
    '''
    estudiantes[nombre] = notas
    print(f"Se agrego estudiante {nombre} con notas {notas}")

agregar_estudiante("Ana", [9, 8, 10])
agregar_estudiante("Luis", [4, 6, 5])
agregar_estudiante("Roberto", [10, 10, 9])

print(f"\n Estudiantes: {estudiantes}\n")

#def promedio_estudiante(nombre):
   # if nombre in estudiantes:
        #notas = estudiantes[nombre]
        #promedio = round(sum(notas) / len(notas) , 2)
        #promedio = round(sum(estudiantes[nombre]) / len(estudiantes[nombre]) , 2)
        #print(f"El promedio de {nombre} es {promedio}")
        #return promedio
   # else:
        #print(f"{nombre} no esta resgitrado como estudiante")

#promedio_estudiante("Ana")
#promedio_estudiante("Luis")
#promedio_estudiante("Roberto")
#promedio_estudiante("Carlitos")

def promedio_estudiante(nombre):
    '''
    nombre: str --> nombre del estudiantte.
    Si el estudiante y sus notas estan en el diccionario, calcula el promedio
    Si el estudiante no esta en el diccionario, muestra el mensaje "El estudiante no se encuentra registrado"
    '''
    notas = estudiantes[nombre]
    promedio = round(sum(notas) / len(notas) , 2)
    #promedio = round(sum(estudiantes[nombre]) / len(estudiantes[nombre]) , 2)
    return promedio

consulta = ["Ana", "Luis", "Roberto", "Carlitos" ]

for nombre in consulta:
    if nombre in estudiantes:
        print(f"El promedio de {nombre} es {promedio_estudiante(nombre)}")
    else:
        print(f"{nombre} no esta resgitrado como estudiante")


def estudiantes_aprobados():
    aprobados = []
    for nombre in estudiantes:
        promedio = promedio_estudiante(nombre)
        if promedio >= 6:
            aprobados.append((nombre, promedio))
    #print(aprobados)
    return aprobados

print("\nEstudiantes aprobados: ")
n = 1
for estudiante, promedio in estudiantes_aprobados():
    print(f"{n}-{estudiante} : promedio {promedio}")
    n +=1


#print(agregar_estudiante.__doc__)



