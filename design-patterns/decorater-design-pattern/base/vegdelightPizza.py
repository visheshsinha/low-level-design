from base import basePizza

class VegdelightPizza(basePizza.BasePizza):
    def __init__(self) -> None:
        self.name = 'Veg Delight'

    def cost(self):
        return 180