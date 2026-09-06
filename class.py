class Shape:
    def __init__(self, color):
        self.color = color
    def get_color(self):
        return self.color
    def get_area(self):
        pass
class Square(Shape):
    def __init__(self, color, side):
        super().__init__(color)
        self.side = side
    def get_area(self):
        return self.side * self.side

sq = Square(input("Enter color of square") , int(input("Enter side length of square")))
print("color:" , sq.get_color())
print("area:" , sq.get_area())