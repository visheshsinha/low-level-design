from shape import shapeInterface
from factory import shapeFactory

if __name__ == '__main__':
    ShapeFactoryObject = shapeFactory.ShapeFactory()
    ShapeObject = ShapeFactoryObject.getShape(input=input())

    if isinstance(ShapeObject, shapeInterface.Shape):
        ShapeObject.draw()
    else:
        print("Entered Shape doesn't exists in factory")