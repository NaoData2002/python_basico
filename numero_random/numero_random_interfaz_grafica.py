import tkinter as tk
from tkinter import messagebox
import random


class JuegoAdivinar:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Juego de Adivinación")
        self.numero_aleatorio = random.randint(1, 100)
        self.intentos = 0
        self.puntuacion = 100

        self.label_adivinar = tk.Label(self.ventana, text="Adivina un número entre 1 y 100")
        self.label_adivinar.pack()

        self.entrada_adivinar = tk.Entry(self.ventana)
        self.entrada_adivinar.bind('<Return>',
                                   self.verificar_adivinanza)  # Al presionar Enter se verifica la adivinanza
        self.entrada_adivinar.pack()

        self.label_resultado = tk.Label(self.ventana, text="")
        self.label_resultado.pack()

        self.label_intentos = tk.Label(self.ventana, text="Intentos: 0")
        self.label_intentos.pack()

        self.label_puntuacion = tk.Label(self.ventana, text="Puntuación: 100")
        self.label_puntuacion.pack()

        self.boton_enviar = tk.Button(self.ventana, text="Enviar", command=self.verificar_adivinanza)
        self.boton_enviar.pack()

    def verificar_adivinanza(self, event=None):
        adivinanza = int(self.entrada_adivinar.get())
        self.intentos += 1
        self.puntuacion -= 10

        if adivinanza == self.numero_aleatorio:
            messagebox.showinfo("¡Felicidades!", "Adivinaste correctamente. El juego se reiniciará ahora.")
            self.numero_aleatorio = random.randint(1, 100)
            self.intentos = 0
            self.puntuacion = 100
            self.label_resultado.config(text="")
        elif adivinanza < self.numero_aleatorio:
            self.label_resultado.config(text="¡Más alto!")
        else:
            self.label_resultado.config(text="¡Más bajo!")

        self.label_intentos.config(text=f"Intentos: {self.intentos}")
        self.label_puntuacion.config(text=f"Puntuación: {max(self.puntuacion, 0)}")
        self.entrada_adivinar.delete(0, 'end')  # Limpia el campo de entrada para el siguiente intento

    def iniciar(self):
        self.ventana.mainloop()


if __name__ == "__main__":
    juego = JuegoAdivinar()
    juego.iniciar()
