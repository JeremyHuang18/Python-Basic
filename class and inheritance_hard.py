import math

class Aircraft():
    next_id = 1
    def __init__(self, aircraft_id, model, fuel_capacity, fuel_comsumption_rate):
        self.aircraft_id = Aircraft.next_id
        self.model = model
        self.fuel_capacity = fuel_capacity
        self.fuel_comsumption_rate = fuel_comsumption_rate
        self.flight_status = 'Inactive'
        self.flight_plan = None
        Aircraft.next_id += 1
        
    def assign_flight_plan(self, FlightPlan):
        # self.flight_plan = {
        #     'origin': origin,
        #     'destination': destination,
        #     'departure_time': departure_time,
        #     'estimated_duration': estimated_duration
        # }
        self.flight_plan = FlightPlan
    
    def update_flight_status(self, flight_status):
        self.flight_status = flight_status

    # def calculate_fuel(self):
    #     return self.fuel_comsumption_rate * self.flight_plan.estimated_duration

    def calculate_fuel(self):
        if not self.flight_plan:
            raise ValueError("No flight plan assigned")
        return self.fuel_comsumption_rate * self.flight_plan.estimated_duration
    
    def simulate_flight(self):
        if not self.flight_plan():
            raise ValueError('No flight plan assigned')
        self.flight_status = 'Flying'
        remaining_time = self.flight_plan.estimated_duration
        while remaining_time > 0:
            print(f"Flying ... Remaining time: {remaining_time} hours")
            self.current_fuel -= self.fuel_comsumption_rate
            remaining_time -= 1
            if self.current_fuel <=0:
                raise ValueError('Fuel Exhausted!')
        self.flight_status = 'Landed'
    
    @staticmethod
    def validation(amount):
        if amount <=0 :
            raise ValueError('Amount must be positive')
    
class PassengerAircraft(Aircraft):
    def __init__(self, aircraft_id, model, fuel_capacity, fuel_comsumption_rate, passenger_capacity):
        super().__init__(aircraft_id, model, fuel_capacity, fuel_comsumption_rate)
        self.passenger_capacity = passenger_capacity
        self.passenger_count = 0

    def board_passengers(self, amount):
        self.validation(amount)
        if self.passenger_count + amount > self.passenger_capacity:
            raise ValueError('Warning: Passenger overload')
        else:
            self.passenger_count += amount
    
    def disembark_passengers(self, amount):
        self.validation(amount)
        if self.passenger_count < amount:
            raise ValueError('Warning: Amount cannot be bigger than current passengers')
        else:
            self.passenger_count -= amount
    
    
class CargoAircraft(Aircraft):
    def __init__(self, aircraft_id, model, fuel_capacity, fuel_comsumption_rate, cargo_capacity):
        super().__init__(aircraft_id, model, fuel_capacity, fuel_comsumption_rate)
        self.cargo_capacity = cargo_capacity
        self.cargo_count = 0

    def load_cargo(self, amount):
        self.validation(amount)
        if self.cargo_count + amount > self.cargo_capacity:
            raise ValueError('Warning: Cargo overload')
        else:
            self.cargo_count += amount
    
    def unload_cargo(self, amount):
        self.validation(amount)
        if self.cargo_count < amount:
            raise ValueError('Warning: Amount cannot be bigger than current cargo')
        else:
            self.cargo_count -= amount

class Drone(Aircraft):
    def __init__(self, aircraft_id, model, fuel_capacity, fuel_comsumption_rate, max_range):
        super().__init__(aircraft_id, model, fuel_capacity, fuel_comsumption_rate)
        self.max_range = max_range

    def check_range(self, distance):
        if distance > self.max_range:
            raise ValueError('Flight distance exceeds maximum range')

class FlightPlan():
    def __init__(self, origin, destination, departure_time, estimated_duration):
        self.origin = origin
        self.destination = destination
        self.departure_time = departure_time
        self.estimated_duration = estimated_duration
    
    def update_destination(self, new_destination):
        self.destination = new_destination
    
    def calculate_distance(self, origin_coords, destination_coords):
        x1, y1 = origin_coords
        x2, y2 = destination_coords
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
