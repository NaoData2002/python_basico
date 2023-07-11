import PySimpleGUI as sg

class AdministradorHogar:
    def __init__(self):
        self.inventario = {}
        self.gastos = {}
        self.presupuesto = 0

    def agregar_a_inventario(self, articulo, cantidad):
        if articulo in self.inventario:
            self.inventario[articulo] += cantidad
        else:
            self.inventario[articulo] = cantidad

    def remover_del_inventario(self, articulo, cantidad):
        if articulo in self.inventario and self.inventario[articulo] >= cantidad:
            self.inventario[articulo] -= cantidad
            if self.inventario[articulo] == 0:
                del self.inventario[articulo]
        else:
            sg.popup("Error: Artículo no encontrado en el inventario o cantidad insuficiente")

    def agregar_gasto(self, categoria, monto):
        if categoria in self.gastos:
            self.gastos[categoria] += monto
        else:
            self.gastos[categoria] = monto

    def establecer_presupuesto(self, presupuesto):
        self.presupuesto = presupuesto

def main():
    administrador = AdministradorHogar()
    sg.theme("LightGreen")

    layout = [
        [sg.Text("Presupuesto:"), sg.Input(size=(15,1), key='-PRESUPUESTO-', enable_events=True)],
        [sg.Text("Artículo:"), sg.Input(size=(15,1), key='-ARTICULO-', enable_events=True), sg.Text("Cantidad:"), sg.Input(size=(15,1), key='-CANTIDAD-', enable_events=True)],
        [sg.Button('Agregar al Inventario'), sg.Button('Eliminar del Inventario')],
        [sg.Text("Categoría del Gasto:"), sg.Input(size=(15,1), key='-CATEGORIA-', enable_events=True), sg.Text("Monto:"), sg.Input(size=(15,1), key='-MONTO-', enable_events=True)],
        [sg.Button('Agregar Gasto')],
        [sg.Output(size=(60,10))],
        [sg.Button('Mostrar Inventario'), sg.Button('Mostrar Gastos'), sg.Button('Mostrar Presupuesto Restante'), sg.Button('Salir')]
    ]

    window = sg.Window('Administración del Hogar', layout)

    while True:
        event, values = window.read()

        if event in (sg.WINDOW_CLOSED, 'Salir'):
            break
        elif event == 'Agregar al Inventario':
            administrador.agregar_a_inventario(values['-ARTICULO-'], int(values['-CANTIDAD-']))
        elif event == 'Eliminar del Inventario':
            administrador.remover_del_inventario(values['-ARTICULO-'], int(values['-CANTIDAD-']))
        elif event == 'Agregar Gasto':
            administrador.agregar_gasto(values['-CATEGORIA-'], float(values['-MONTO-']))
        elif event == '-PRESUPUESTO-':
            administrador.establecer_presupuesto(float(values['-PRESUPUESTO-']))
        elif event == 'Mostrar Inventario':
            print("\nInventario Actual:")
            for item, cantidad in administrador.inventario.items():
                print(f"{item}: {cantidad}")
        elif event == 'Mostrar Gastos':
            print("\nGastos Actuales:")
            for categoria, monto in administrador.gastos.items():
                print(f"{categoria}: {monto}")
        elif event == 'Mostrar Presupuesto Restante':
            presupuesto_restante = administrador.presupuesto - sum(administrador.gastos.values())
            print(f"\nPresupuesto Restante: {presupuesto_restante}")

    window.close()

if __name__ == "__main__":
    main()
