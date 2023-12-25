from shape import shapeInterface

class Rectangle(shapeInterface.Shape):
    def __init__(self) -> None:
        pass

    def draw(self):
        print('Drawing a RECTANGLE')
        return