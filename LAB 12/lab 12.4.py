class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

    def perimeter(self):
        return 4 * self.side


sq = Square(5)
print("Area of square:", sq.area())
print("Perimeter of square:", sq.perimeter())
