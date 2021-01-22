class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    # def __str__(self):
    #     return f"Total {self.name} is {function below???}

    def fare(self):
        return self.capacity * 100


class Bus(Vehicle):
    def fare(self):
        return super().fare() * 1.1  # add 10 % of the fare


class A:
    pass


class B:
    pass


class C(A, B):
    pass


School_bus = Bus("School Volvo", 12, 50)
print("Total Bus fare is:", School_bus.fare())

print("____________________")

print("Is \"School bus\" instance of Bus --", isinstance(School_bus, Bus))
print("Is \"School bus\" instance of Vehicle --",
      isinstance(School_bus, Vehicle))
print("Is \"Bus\" a subclass of Vehicle --", issubclass(Bus, Vehicle))
print("Is \"Vehicle\" a subclass of Bus --", issubclass(Vehicle, Bus))

print("____________________")

print(C.__bases__)
