import tkinter as tk
from tkinter import ttk, filedialog, messagebox, colorchooser
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import pandas as pd


class GraphGenerator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Generador de Gráficos")
        self.frame = ttk.Frame(self.window)
        self.frame.pack()

        self.file_button = ttk.Button(self.frame, text="Cargar Archivo CSV", command=self.load_file)
        self.file_button.pack(side=tk.LEFT)

        self.column1 = ttk.Combobox(self.frame, values=[])
        self.column1.pack(side=tk.LEFT)

        self.column2 = ttk.Combobox(self.frame, values=[])
        self.column2.pack(side=tk.LEFT)

        self.graph_button = ttk.Button(self.frame, text="Generar Gráfico", command=self.generate_graph)
        self.graph_button.pack(side=tk.LEFT)

        self.graph_type = ttk.Combobox(self.frame, values=["line", "bar", "scatter", "hist", "box", "pie"])
        self.graph_type.pack(side=tk.LEFT)

        self.title_entry = tk.Entry(self.frame)
        self.title_entry.pack(side=tk.LEFT)
        self.title_entry.insert(0, "Título del Gráfico")

        self.xlabel_entry = tk.Entry(self.frame)
        self.xlabel_entry.pack(side=tk.LEFT)
        self.xlabel_entry.insert(0, "Etiqueta Eje X")

        self.ylabel_entry = tk.Entry(self.frame)
        self.ylabel_entry.pack(side=tk.LEFT)
        self.ylabel_entry.insert(0, "Etiqueta Eje Y")

        self.color_button = ttk.Button(self.frame, text="Seleccionar color", command=self.select_color)
        self.color_button.pack(side=tk.LEFT)

        self.figure = plt.figure(figsize=(5, 4), dpi=100)
        self.canvas = FigureCanvasTkAgg(self.figure, master=self.window)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        self.toolbar = NavigationToolbar2Tk(self.canvas, self.window)
        self.toolbar.update()
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        self.data = pd.DataFrame()
        self.graph_color = "blue"

    def load_file(self):
        filename = filedialog.askopenfilename(initialdir="/", title="Selecciona un archivo CSV",
                                              filetypes=(("Archivos CSV", "*.csv"), ("Todos los archivos", "*.*")))
        if filename:
            self.data = pd.read_csv(filename)
            self.column1['values'] = self.data.columns.tolist()
            self.column2['values'] = self.data.columns.tolist()

    def generate_graph(self):
        if self.data.empty:
            messagebox.showinfo("No hay datos", "Carga un archivo CSV primero.")
            return

        graph_type = self.graph_type.get()
        column1 = self.column1.get()
        column2 = self.column2.get()

        if not graph_type or not column1:
            messagebox.showinfo("Información faltante",
                                "Asegúrate de haber seleccionado el tipo de gráfico y las columnas.")
            return

        self.figure.clear()
        ax = self.figure.add_subplot(111)

        if graph_type in ["line", "bar", "area"]:
            self.data.plot(kind=graph_type, x=column1, y=column2, ax=ax, color=self.graph_color)
        elif graph_type == "scatter":
            self.data.plot(kind='scatter', x=column1, y=column2, ax=ax, color=self.graph_color)
        elif graph_type == "hist":
            self.data[column1].plot(kind='hist', ax=ax, color=self.graph_color)
        elif graph_type == "box":
            self.data[column1].plot(kind='box', ax=ax, color=self.graph_color)
        elif graph_type == "pie":
            self.data[column1].plot(kind='pie', ax=ax)

        ax.set_title(self.title_entry.get())
        ax.set_xlabel(self.xlabel_entry.get())
        ax.set_ylabel(self.ylabel_entry.get())

        self.canvas.draw()

    def select_color(self):
        color_code = colorchooser.askcolor(title="Elige un color")
        self.graph_color = color_code[1]

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    app = GraphGenerator()
    app.run()
