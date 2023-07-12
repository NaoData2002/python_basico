import PySimpleGUI as sg
from fuentes import *
from apa import APA

def main():
    layout = [
        [sg.Combo(['Libro', 'Artículo', 'Video de Internet', 'Imagen de Internet'], key='-TIPO-', enable_events=True, readonly=True, size=(20, 1))],
        [sg.Text('Autor'), sg.Input(key='-AUTOR-')],
        [sg.Text('Título'), sg.Input(key='-TITULO-')],
        [sg.Text('Año'), sg.Input(key='-AÑO-')],
        [sg.Text('Editorial'), sg.Input(key='-EDITORIAL-', visible=False)],
        [sg.Text('Ciudad'), sg.Input(key='-CIUDAD-', visible=False)],
        [sg.Text('Revista'), sg.Input(key='-REVISTA-', visible=False)],
        [sg.Text('Volumen'), sg.Input(key='-VOLUMEN-', visible=False)],
        [sg.Text('Número'), sg.Input(key='-NUMERO-', visible=False)],
        [sg.Text('Páginas'), sg.Input(key='-PAGINAS-', visible=False)],
        [sg.Text('Sitio'), sg.Input(key='-SITIO-', visible=False)],
        [sg.Text('URL'), sg.Input(key='-URL-', visible=False)],
        [sg.Button('Generar cita')]
    ]

    window = sg.Window('Generador de citas APA', layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == '-TIPO-':
            if values['-TIPO-'] == 'Libro':
                window['-EDITORIAL-'].update(visible=True)
                window['-CIUDAD-'].update(visible=True)
                window['-REVISTA-'].update(visible=False)
                window['-VOLUMEN-'].update(visible=False)
                window['-NUMERO-'].update(visible=False)
                window['-PAGINAS-'].update(visible=False)
                window['-SITIO-'].update(visible=False)
                window['-URL-'].update(visible=False)
            elif values['-TIPO-'] == 'Artículo':
                window['-EDITORIAL-'].update(visible=False)
                window['-CIUDAD-'].update(visible=False)
                window['-REVISTA-'].update(visible=True)
                window['-VOLUMEN-'].update(visible=True)
                window['-NUMERO-'].update(visible=True)
                window['-PAGINAS-'].update(visible=True)
                window['-SITIO-'].update(visible=False)
                window['-URL-'].update(visible=False)
            elif values['-TIPO-'] in ['Video de Internet', 'Imagen de Internet']:
                window['-EDITORIAL-'].update(visible=False)
                window['-CIUDAD-'].update(visible=False)
                window['-REVISTA-'].update(visible=False)
                window['-VOLUMEN-'].update(visible=False)
                window['-NUMERO-'].update(visible=False)
                window['-PAGINAS-'].update(visible=False)
                window['-SITIO-'].update(visible=True)
                window['-URL-'].update(visible=True)
        elif event == 'Generar cita':
            try:
                fuente = crear_fuente(values)
                cita = APA.citar(fuente)
                sg.popup('La cita generada es:', cita)
            except Exception as e:
                sg.popup('Error:', str(e))

    window.close()

def crear_fuente(values):
    autor = values['-AUTOR-']
    titulo = values['-TITULO-']
    año = values['-AÑO-']
    if values['-TIPO-'] == 'Libro':
        editorial = values['-EDITORIAL-']
        ciudad = values['-CIUDAD-']
        return Libro(autor, titulo, año, editorial, ciudad)
    elif values['-TIPO-'] == 'Artículo':
        revista = values['-REVISTA-']
        volumen = values['-VOLUMEN-']
        numero = values['-NUMERO-']
        paginas = values['-PAGINAS-']
        return Articulo(autor, titulo, año, revista, volumen, numero, paginas)
    elif values['-TIPO-'] in ['Video de Internet', 'Imagen de Internet']:
        sitio = values['-SITIO-']
        url = values['-URL-']
        if values['-TIPO-'] == 'Video de Internet':
            return VideoInternet(autor, titulo, año, sitio, url)
        else:
            return ImagenInternet(autor, titulo, año, sitio, url)

if __name__ == "__main__":
    main()
