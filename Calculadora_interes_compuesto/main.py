import matplotlib.pyplot as plt
import PySimpleGUI as sg
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from interest_calculator import InterestCalculator
import os


def draw_figure(canvas, figure):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
    return figure_canvas_agg


def main():
    sg.theme('DarkAmber')

    history = []  # For storing history of investment calculations

    layout = [
        [sg.Text("Monto inicial"), sg.Input(key='-MONTO-', size=(10, 1))],
        [sg.Text("Tasa de interés (%)"), sg.Input(key='-TASA-', size=(10, 1))],
        [sg.Text("Período de tiempo (años)"), sg.Input(key='-TIEMPO-', size=(10, 1))],
        [sg.Text("Monto de reinversión"), sg.Input(key='-REINVERSION-', size=(10, 1))],
        [sg.Text("Periodo de reinversión"),
         sg.Combo(['Mensual', 'Trimestral', 'Semestral', 'Anual'], key='-PERIODO-', default_value='Anual')],
        [sg.Text("Divisa"), sg.Combo(
            ['USD', 'EUR', 'GBP', 'JPY', 'CAD', 'AUD', 'NZD', 'BRL', 'ARS', 'COP', 'CLP', 'MXN', 'UYU', 'VEF', 'PYG',
             'BOB', 'PEN', 'ZAR', 'INR', 'RUB', 'TRY', 'KRW', 'IDR'], key='-DIVISA-', default_value='USD')],
        [sg.Text("Tipo de interés"), sg.Combo(['Anual', 'Mensual'], key='-TIPO-', default_value='Anual')],
        [sg.Button('Calcular'), sg.Button('Historial'), sg.Button('Exportar Gráfico'), sg.Button('Salir')],
        [sg.Canvas(key='-CANVAS-')]
    ]

    window = sg.Window('Calculadora de Interés Compuesto', layout)

    while True:
        event, values = window.read()

        if event == 'Salir' or event == sg.WINDOW_CLOSE_ATTEMPTED_EVENT:
            break

        elif event == 'Calcular':
            initial_amount = float(values['-MONTO-'])
            interest_rate = float(values['-TASA-'])
            time = int(values['-TIEMPO-'])
            reinvestment = float(values['-REINVERSION-'])
            reinvestment_period = values['-PERIODO-']
            currency = values['-DIVISA-']
            interest_type = values['-TIPO-']

            calc = InterestCalculator(initial_amount, interest_rate, time, currency, interest_type, reinvestment,
                                      reinvestment_period)
            final_amount, growth, investment_evolution = calc.calculate_compound_interest()

            sg.popup(
                f"El monto final después de {time} años es: {final_amount:.2f} {currency}\nEl crecimiento de la inversión es: {growth:.2f} {currency}")

            # Store the calculation history
            history.append(
                f"Inicial: {initial_amount} {currency}, Tasa: {interest_rate}%, Tiempo: {time} años, Reversión: {reinvestment}, Monto final: {final_amount:.2f} {currency}")

            fig, ax = plt.subplots()
            ax.plot(investment_evolution)
            ax.set_title('Evolución de la inversión')
            ax.set_xlabel('Período')
            ax.set_ylabel('Inversión (' + currency + ')')

            if window['-CANVAS-'].TKCanvas.winfo_children():
                for widget in window['-CANVAS-'].TKCanvas.winfo_children():
                    widget.destroy()
            draw_figure(window['-CANVAS-'].TKCanvas, fig)

        elif event == 'Historial':
            sg.popup_scrolled(history, title="Historial de Cálculos")

        elif event == 'Exportar Gráfico':
            filename = sg.popup_get_file('Guardar gráfico como', save_as=True, default_extension=".png",
                                         file_types=(('PNG', '.png'), ('JPEG', '.jpg'), ('SVG', '.svg'), ('PDF', '.pdf')))
            if filename:
                fig.savefig(filename)

    window.close()


if __name__ == "__main__":
    main()
