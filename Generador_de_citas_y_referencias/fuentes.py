class Fuente:
    def __init__(self, autor, titulo, año):
        self.autor = autor
        self.titulo = titulo
        self.año = año

class Libro(Fuente):
    def __init__(self, autor, titulo, año, editorial, ciudad):
        super().__init__(autor, titulo, año)
        self.editorial = editorial
        self.ciudad = ciudad

    def citar_apa(self):
        return f"{self.autor} ({self.año}). {self.titulo}. {self.ciudad}: {self.editorial}."

class Articulo(Fuente):
    def __init__(self, autor, titulo, año, revista, volumen, numero, paginas):
        super().__init__(autor, titulo, año)
        self.revista = revista
        self.volumen = volumen
        self.numero = numero
        self.paginas = paginas

    def citar_apa(self):
        return f"{self.autor} ({self.año}). {self.titulo}. {self.revista}, {self.volumen}({self.numero}), {self.paginas}."

class VideoInternet(Fuente):
    def __init__(self, autor, titulo, año, sitio, url):
        super().__init__(autor, titulo, año)
        self.sitio = sitio
        self.url = url

    def citar_apa(self):
        return f"{self.autor} ({self.año}). {self.titulo}. {self.sitio}. {self.url}."

class ImagenInternet(Fuente):
    def __init__(self, autor, titulo, año, sitio, url):
        super().__init__(autor, titulo, año)
        self.sitio = sitio
        self.url = url

    def citar_apa(self):
        return f"{self.autor} ({self.año}). {self.titulo}. {self.sitio}. {self.url}."

# Añade aquí las demás fuentes.
