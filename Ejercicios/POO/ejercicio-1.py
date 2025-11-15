# 1 – Herencia en la Creación de Clases {
# En este ejercicio, vas a practicar el concepto de herencia en Python. Crearás una clase base
# llamada Persona y luego, crearás una clase hija llamada Estudiante que herede de Persona.
# El objetivo es reutilizar el código de la clase base y extenderlo con funcionalidades
# adicionales en la clase hija
# Requerimientos:
# 1- Clase Persona:
# * Debe tener dos atributos: nombre y apellido.
# * Debe tener un método nombre_completo() que retorne el nombre completo de la
# persona, en formato “nombre apellido”
# 2- Clase Estudiante:
# * Debe heredar de la clase Persona
# * Debe agregar un atributo adicional carrera que almacene la carrera que está
# estudiando el estudiante.
# * Debe tener un método obtener_carrera() que retorne un mensaje indicando la
# carrera que está estudiando el estudiante. El formato del mensaje debe ser: “Está
# estudiando la carrara de {carrera}”.
# 3- Ejemplo de uso:
# * Crea una instancia de la clase Persona y llama al método nombre_completo() para
# mostrar su nombre completo.
# * Crea una instancia de la clase Estudiante y llama a los métodos nombre_completo()
# y obtener_carrera() para mostrar tanto el nombre completo del estudiante como la
# carrera que está estudiando.
# }

class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
    
    def nombre_completo(self):
        return f"{self.nombre} {self.apellido}"
        
class Estudiante(Persona):
    def __init__(self, nombre, apellido, carrera):
        super().__init__(nombre, apellido)
        self.carrera = carrera

    def obtener_carrera(self):
        return f"Esta estudiando la carrera {self.carrera}"
    
persona1 = Persona('Martin', 'Romero')
print(persona1.nombre_completo())

estudiante1= Estudiante('Martin','Romero', 'IEM')
print('\n')
print(estudiante1.nombre_completo())
print(estudiante1.obtener_carrera())



