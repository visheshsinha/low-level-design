from base import basePizza

class FarmhousePizza(basePizza.BasePizza):
    def __init__(self) -> None:
        self.name = 'FarmHouse'

    def cost(self):
        return 200