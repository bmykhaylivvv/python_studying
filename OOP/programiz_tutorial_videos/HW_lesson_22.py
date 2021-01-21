class Polygon:
    def __init__(self, sides):
        self.sides = sides

    def __str__(self):
        return "A polygon is a two dimersional shape with straight line"

    def get_perimetr(self):
        perimeter = sum(self.sides)
        return perimeter

class Triangle(Polygon):
    def __str__(self):
        return "A triagle is a polygon with 3 edges"

class Quodrilateral(Polygon):
    def __str__(self):
        return "A quodrilateral is a polygon with 4 edges"


t1 = Triangle([5, 6, 7])

print(t1)

perimeter = t1.get_perimetr()
print("The peremeter is", perimeter)

