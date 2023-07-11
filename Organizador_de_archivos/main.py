import PySimpleGUI as sg
from organizador import Organizador
from renombrador import Renombrador

def main():
    layout = [[sg.Text("Seleccione el directorio para organizar/renombrar:"),
               sg.Input(key='-IN-', enable_events=True),
               sg.FolderBrowse()],
              [sg.Text("Elige cómo organizar los archivos:"),
               sg.Combo(['Extension', 'Fecha', 'Tamaño'], key='-METODO-')],
              [sg.Text("Nombre personalizado para las carpetas:"),
               sg.Input(key='-NOMBRE CARPETA-')],
              [sg.Text("Nuevo nombre para renombrar archivos:"),
               sg.Input(key='-NOMBRE ARCHIVOS-')],
              [sg.Output(size=(60, 20), key='-OUTPUT-')],
              [sg.Button('Organizar'), sg.Button('Renombrar'), sg.Button('Salir')]]

    window = sg.Window('Organizador y Renombrador de Archivos', layout)

    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED or event == 'Salir':
            break
        if event == 'Organizar':
            if values['-IN-'] and values['-METODO-'] and values['-NOMBRE CARPETA-']:
                organizador = Organizador(values['-IN-'], values['-METODO-'], values['-NOMBRE CARPETA-'])
                for mensaje in organizador.organizar():
                    window['-OUTPUT-'].update(mensaje)
            else:
                sg.popup("Por favor, rellene todos los campos para organizar")
        if event == 'Renombrar':
            if values['-IN-'] and values['-NOMBRE ARCHIVOS-']:
                renombrador = Renombrador(values['-IN-'], values['-NOMBRE ARCHIVOS-'])
                for mensaje in renombrador.renombrar():
                    window['-OUTPUT-'].update(mensaje)
            else:
                sg.popup("Por favor, rellene todos los campos para renombrar")
    window.close()

if __name__ == "__main__":
    main()
