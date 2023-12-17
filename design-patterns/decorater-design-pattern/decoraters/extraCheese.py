from decoraters import toppingPizza
from base import basePizza

class ExtraCheese(toppingPizza.Topping):
    def __init__(self, pizza: basePizza.BasePizza) -> None:
        self.pizza = pizza
        self.name = 'Extra Cheese'
    
    def cost(self):
        if isinstance(self.pizza, toppingPizza.Topping):
            return self.pizza.cost() + 20
        else:
            return self.pizza().cost() + 20