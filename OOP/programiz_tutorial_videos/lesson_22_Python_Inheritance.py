class Polygon:
    def __init__(self, sides):
        self.sides = sides

    def display_info(self):
        print("A polygon is a two dimersional shape with straight line")

    def get_perimetr(self):
        perimeter = sum(self.sides)
        return perimeter

class Triangle(Polygon):
    def display_info(self):
        print("A triagle is a polygon with 3 edges")
        super().display_info()

class Quodrilateral(Polygon):
    def display_info(self):
        print("A quodrilateral is a polygon with 4 edges")


t1 = Triangle([5, 6, 7])

perimeter = t1.get_perimetr()

print("The peremeter is", perimeter)

t1.display_info()