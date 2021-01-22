class Vehicle:
    def __init__(self, category, color, paint_thickness):
        self.category = category
        self.color = color
        self.paint_thickness = paint_thickness

class Car(Vehicle):
    def __init__(self, category, make, model, color, paint_thickness, horsepower):
        self.make = make
        self.model = model
        self.horsepower = horsepower
        super(Car, self).__init__(category, color, paint_thickness)

    def quality_check(self):
        if 80 < self.paint_thickness < 99 and 244 < self.horsepower < 399:
            return f"{self.make} {self.model} is a good car with {self.horsepower} horsepower"
        return "You should find a better car"


car1 = Car("car", "BMW", "328i", "white", 85, 245)
print(car1.__dict__)
print("______________")
print(car1.quality_check())
