class Vehicle:
    def __init__(self, name, max_speed, mileage, color = "White"):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        self.color = color

    def __str__(self):
        return f"Color: {self.color}, Vehicle name: {self.name}, Speed: {self.max_speed}, Mileage: {self.mileage}"

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"

        

class Bus(Vehicle):
    def seating_capacity(self, capacity = 100):
        return super().seating_capacity(capacity)

class Car(Vehicle):
    pass


School_bus = Bus("School Volvo", 12, 50)
print("Total Bus fare is:", School_bus.fare())
