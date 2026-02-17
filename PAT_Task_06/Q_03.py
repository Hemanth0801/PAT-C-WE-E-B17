class Vehicle:
    def __init__(self, model, rental_rate):
        self.model = model
        self.rental_rate = rental_rate
    def calculate_rental(self, days):
        return self.rental_rate * days

class Car(Vehicle):
    def __init__(self, model, rental_rate, insurance_fee):
        super().__init__(model, rental_rate)
        self.insurance_fee = insurance_fee

    def calculate_rental(self, days):
        return (self.rental_rate * days) + self.insurance_fee

class Bike(Vehicle):
    def __init__(self, model, rental_rate, helmet_fee):
        super().__init__(model, rental_rate)
        self.helmet_fee = helmet_fee

    def calculate_rental(self, days):
        return (self.rental_rate * days) + self.helmet_fee

class Truck(Vehicle):
    def __init__(self, model, rental_rate, load_charge):
        super().__init__(model, rental_rate)
        self.load_charge = load_charge

    def calculate_rental(self, days):
        return (self.rental_rate * days) + self.load_charge


v1 = Car("Hyundai i20", 2000, 500)
v2 = Bike("pulsar 220", 800, 100)
v3 = Truck("Tata", 4000, 1500)

vehicles = [v1, v2, v3]

for vehicle in vehicles:
    print("Vehicle Model:", vehicle.model)
    print("Total Rental Cost for 3 days:", vehicle.calculate_rental(3))