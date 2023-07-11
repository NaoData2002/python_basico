import os

class Renombrador:
    def __init__(self, directorio, nombre):
        self.directorio = directorio
        self.nombre = nombre

    def renombrar(self):
        archivos = os.listdir(self.directorio)

        for i, archivo in enumerate(archivos):
            ruta_archivo = os.path.join(self.directorio, archivo)

            if os.path.isfile(ruta_archivo):
                _, extension = os.path.splitext(archivo)
                nuevo_nombre = f"{self.nombre}_{i}{extension}"
                os.rename(ruta_archivo, os.path.join(self.directorio, nuevo_nombre))

                yield f"Archivo {archivo} renombrado a {nuevo_nombre}"

        yield "¡Archivos renombrados correctamente!"
