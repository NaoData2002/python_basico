import csv

class Database:
    def __init__(self):
        self.drivers = {}
        self.vehicles = {}
        self.trips = []

    def add_driver(self, name, phone, location):
        driver_id = len(self.drivers) + 1
        self.drivers[driver_id] = {'name': name, 'phone': phone, 'location': location}

    def delete_driver(self, driver_id):
        if driver_id in self.drivers:
            del self.drivers[driver_id]

    def add_vehicle(self, plate):
        vehicle_id = len(self.vehicles) + 1
        self.vehicles[vehicle_id] = plate

    def add_trip(self, driver_id, vehicle_id, date, distance):
        self.trips.append({'driver_id': driver_id, 'vehicle_id': vehicle_id, 'date': date, 'distance': distance})

    def get_trips(self, driver_id):
        return [trip for trip in self.trips if trip['driver_id'] == driver_id]

    def get_drivers(self):
        return self.drivers.items()

    def get_vehicles(self):
        return self.vehicles.items()

    def export_csv(self, filename):
        with open(filename, 'w', newline='') as csvfile:
            fieldnames = ['Driver ID', 'Vehicle ID', 'Date', 'Distance']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for trip in self.trips:
                writer.writerow({'Driver ID': trip['driver_id'], 'Vehicle ID': trip['vehicle_id'], 'Date': trip['date'], 'Distance': trip['distance']})
