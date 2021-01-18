class Car:
    def __init__(self, color, kilometers):
        self.color = color
        self.kilometers = kilometers

    def __str__(self):
        return f'The {self.color} car has {self.kilometers:,} kilometers'


blue_car = Car(color='blue', kilometers=20_000)
red_car = Car(color='red', kilometers=30_000)

print(blue_car)
print(red_car)
