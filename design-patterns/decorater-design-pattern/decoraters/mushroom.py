from decoraters import toppingPizza
from base import basePizza

class Mushroom(toppingPizza.Topping):
    def __init__(self, pizza: basePizza.BasePizza) -> None:
        self.pizza = pizza
        self.name = 'Mushroom'
    
    def cost(self):
        if isinstance(self.pizza, toppingPizza.Topping):
            return self.pizza.cost() + 10
        else:
            return self.pizza().cost() + 10