import PySimpleGUI as sg
from datetime import datetime
from database import Database

class Application:
    def __init__(self, db):
        self.db = db
        self.window = sg.Window('Registro de Kilometraje', self.layout(), finalize=True)

    def layout(self):
        return [
            [sg.Text('Nombre del Conductor:'), sg.Input(key='-NAME-')],
            [sg.Text('Número de Teléfono:'), sg.Input(key='-PHONE-')],
            [sg.Text('Ubicación:'), sg.Input(key='-LOCATION-')],
            [sg.Button('Añadir Conductor'), sg.Button('Eliminar Conductor')],
            [sg.Listbox(values=[], size=(50, 10), key='-DRIVER LIST-')],
            [sg.Text('Placa del Vehículo:'), sg.Input(key='-PLATE-')],
            [sg.Button('Añadir Vehículo')],
            [sg.Listbox(values=[], size=(50, 10), key='-VEHICLE LIST-')],
            [sg.Text('Fecha del Recorrido:'), sg.Input(key='-DATE-', disabled=True), sg.CalendarButton('Seleccionar Fecha', target='-DATE-', format='%d-%m-%Y')],
            [sg.Text('Kilometraje Total:'), sg.Input(key='-DISTANCE-')],
            [sg.Button('Añadir Recorrido')],
            [sg.Button('Mostrar Recorridos del Conductor')],
            [sg.Button('Exportar a CSV')]
        ]

    def run(self):
        while True:
            event, values = self.window.read()
            if event == sg.WINDOW_CLOSED:
                break
            elif event == 'Añadir Conductor':
                self.db.add_driver(values['-NAME-'], values['-PHONE-'], values['-LOCATION-'])
            elif event == 'Eliminar Conductor':
                if values['-DRIVER LIST-']:
                    selected_driver = values['-DRIVER LIST-'][0]
                    driver_id = int(selected_driver.split()[0])
                    self.db.delete_driver(driver_id)
                else:
                    sg.popup('Por favor, selecciona un conductor para eliminar.')
            elif event == 'Añadir Vehículo':
                self.db.add_vehicle(values['-PLATE-'])
            elif event == 'Añadir Recorrido':
                if values['-DRIVER LIST-'] and values['-VEHICLE LIST-']:
                    selected_driver = values['-DRIVER LIST-'][0]
                    driver_id = int(selected_driver.split()[0])
                    selected_vehicle = values['-VEHICLE LIST-'][0]
                    vehicle_id = int(selected_vehicle.split()[0])
                    date = datetime.strptime(values['-DATE-'], '%d-%m-%Y').date()
                    distance = int(values['-DISTANCE-'])
                    self.db.add_trip(driver_id, vehicle_id, date, distance)
                else:
                    sg.popup('Por favor, selecciona un conductor y un vehículo para añadir un recorrido.')
            elif event == 'Mostrar Recorridos del Conductor':
                if values['-DRIVER LIST-']:
                    selected_driver = values['-DRIVER LIST-'][0]
                    driver_id = int(selected_driver.split()[0])
                    self.show_trips(driver_id)
                else:
                    sg.popup('Por favor, selecciona un conductor para mostrar sus recorridos.')
            elif event == 'Exportar a CSV':
                self.db.export_csv('registro.csv')
                sg.popup('Datos exportados correctamente.')

            drivers = self.db.get_drivers()
            drivers_list = [f"{driver[0]} {driver[1]['name']} {driver[1]['phone']} {driver[1]['location']}" for driver in drivers]
            self.window['-DRIVER LIST-'].update(values=drivers_list)

            vehicles = self.db.get_vehicles()
            vehicles_list = [f"{vehicle[0]} {vehicle[1]}" for vehicle in vehicles]
            self.window['-VEHICLE LIST-'].update(values=vehicles_list)

        self.window.close()

    def show_trips(self, driver_id):
        trips = self.db.get_trips(driver_id)
        trip_text = '\n'.join(f"Fecha: {trip['date']}, Distancia: {trip['distance']}" for trip in trips)
        sg.popup(trip_text)

db = Database()
app = Application(db)
app.run()

