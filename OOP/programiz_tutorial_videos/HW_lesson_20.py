class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __str__(self):
        return (f"Sides: {self.a} {self.b} {self.c}")

    def perimeter(self):
        perimtr = self.a + self.b + self.c
        return perimtr

triangle1 = Triangle(12, 9, 2)
triangle2 = Triangle(a = 10, b = 2, c = 2)

print(triangle1)
print("Perimetr =", triangle1.perimeter())

print()

print(triangle2)
print("Perimetr =", triangle2.perimeter())




