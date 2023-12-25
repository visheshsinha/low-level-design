from shape import circle, rectangle, shapeInterface

class ShapeFactory:
    def __init__(self) -> None:
        pass

    def getShape(self, input: str) -> shapeInterface.Shape:
        input = input.lower()
        shapes = {
            'circle': circle.Circle(),
            'rectangle': rectangle.Rectangle() 
        }

        if input in shapes:
            return shapes[input]
        else:
            return None