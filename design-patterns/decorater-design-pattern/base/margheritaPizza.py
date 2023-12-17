from base import basePizza

class MargheritaPizza(basePizza.BasePizza):
    def __init__(self) -> None:
        self.name = 'Margherita'

    def cost(self):
        return 150