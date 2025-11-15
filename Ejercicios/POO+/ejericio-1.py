class Libro:
    def __init__(self, titulo, autor, isbn, paginas, genero):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.paginas = paginas
        self.genero = genero
        self._prestado = False   # atributo encapsulado

    def prestar(self):
        if self._prestado:
            return f"El libro '{self.titulo}' ya está prestado."
        self._prestado = True
        return f"Libro '{self.titulo}' prestado con éxito."

    def devolver(self):
        if not self._prestado:
            return f"El libro '{self.titulo}' no estaba prestado."
        self._prestado = False
        return f"Libro '{self.titulo}' devuelto con éxito."

    def esta_prestado(self):
        return self._prestado

    def info(self):
        return f"{self.titulo} ({self.genero}) - {self.paginas} páginas."


class LibroElectronico(Libro):
    def __init__(self, titulo, autor, isbn, paginas, genero, tamaño_mb):
        super().__init__(titulo, autor, isbn, paginas, genero)
        self.tamaño_mb = tamaño_mb

    def info(self):  # Polimorfismo
        return f"{self.titulo} - Ebook de {self.tamaño_mb} MB"


class LibroAudiovisual(Libro):
    def __init__(self, titulo, autor, isbn, paginas, genero, duracion_min):
        super().__init__(titulo, autor, isbn, paginas, genero)
        self.duracion = duracion_min

    def info(self):  # Polimorfismo
        return f"{self.titulo} - Audiolibro de {self.duracion} minutos"


class Autor:
    def __init__(self, nombre, nacionalidad, fecha_nac):
        self.nombre = nombre
        self.nacionalidad = nacionalidad
        self.fecha_nac = fecha_nac
        self.libros_publicados = []

    def publicar_libro(self, libro):
        self.libros_publicados.append(libro)
        return f"El autor {self.nombre} publicó '{libro.titulo}'."


class Lector:
    def __init__(self, nombre, edad, direccion, numero_socio):
        self.nombre = nombre
        self.edad = edad
        self.direccion = direccion
        self.nro_socio = numero_socio
        self.libros_prestados = []

    def solicitar_prestamo(self, libro):
        if libro.esta_prestado():
            return f"El libro '{libro.titulo}' no está disponible."
        libro.prestar()
        self.libros_prestados.append(libro)
        return f"{self.nombre} pidió prestado '{libro.titulo}'."

    def devolver_libro(self, libro):
        if libro not in self.libros_prestados:
            return f"{self.nombre} no tenía ese libro."
        libro.devolver()
        self.libros_prestados.remove(libro)
        return f"{self.nombre} devolvió '{libro.titulo}'."


class Libreria:
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros = []
        self.lectores = []
        self.autores = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def registrar_lector(self, lector):
        self.lectores.append(lector)

    def registrar_autor(self, autor):
        self.autores.append(autor)

    def buscar_libro(self, titulo):
        for libro in self.libros:
            if libro.titulo.lower() == titulo.lower():
                return libro
        return None

    def prestar_libro(self, lector, titulo):
        libro = self.buscar_libro(titulo)
        if not libro:
            return "El libro no existe."
        return lector.solicitar_prestamo(libro)

    def devolver_libro(self, lector, titulo):
        libro = self.buscar_libro(titulo)
        if not libro:
            return "El libro no existe."
        return lector.devolver_libro(libro)

autor = Autor("J.K. Rowling", "Británica", "1965")
libro1 = Libro("Harry Potter", autor, "1111", 450, "Fantasía")
ebook = LibroElectronico("Harry Potter Ebook", autor, "2222", 450, "Fantasía", 12)
audio = LibroAudiovisual("Harry Potter Audio", autor, "3333", 0, "Fantasía", 120)

autor.publicar_libro(libro1)

lector = Lector("Martin", 30, "Buenos Aires", 101)

libreria = Libreria("Libroteca")
libreria.registrar_autor(autor)
libreria.registrar_lector(lector)
libreria.agregar_libro(libro1)
libreria.agregar_libro(ebook)
libreria.agregar_libro(audio)

print(libreria.prestar_libro(lector, "Harry Potter"))
print(libreria.devolver_libro(lector, "Harry Potter"))

