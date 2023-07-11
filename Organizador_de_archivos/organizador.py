import os
import shutil
import time


class Organizador:
    def __init__(self, directorio, metodo, nombre_carpeta):
        self.directorio = directorio
        self.metodo = metodo
        self.nombre_carpeta = nombre_carpeta

    def organizar(self):
        archivos = os.listdir(self.directorio)

        for archivo in archivos:
            ruta_archivo = os.path.join(self.directorio, archivo)

            if os.path.isfile(ruta_archivo):
                if self.metodo == 'Extension':
                    _, extension = os.path.splitext(archivo)
                    nombre_subcarpeta = extension[1:].upper() + "s"
                elif self.metodo == 'Fecha':
                    timestamp = os.path.getmtime(ruta_archivo)
                    fecha_creacion = time.strftime('%Y-%m-%d', time.localtime(timestamp))
                    nombre_subcarpeta = fecha_creacion + "s"
                elif self.metodo == 'Tamaño':
                    tamaño = os.path.getsize(ruta_archivo)
                    if tamaño < 1000000:  # Menos de 1MB
                        nombre_subcarpeta = 'Pequeños'
                    elif tamaño < 1000000000:  # Menos de 1GB
                        nombre_subcarpeta = 'Medianos'
                    else:
                        nombre_subcarpeta = 'Grandes'

                carpeta_destino = os.path.join(self.directorio, self.nombre_carpeta, nombre_subcarpeta)
                if not os.path.exists(carpeta_destino):
                    os.makedirs(carpeta_destino)
                shutil.move(ruta_archivo, carpeta_destino)

                yield f"Archivo {archivo} movido a {carpeta_destino}"

        yield "¡Archivos organizados correctamente!"
