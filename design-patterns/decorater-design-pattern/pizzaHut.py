from base import basePizza, farmhousePizza, margheritaPizza, vegdelightPizza
from decoraters import toppingPizza, mushroom, extraCheese

class PizzaHut:
    def __init__(self) -> None:
        self.pizza = None

    def basing(self, pizza: basePizza.BasePizza) -> None:
        print(f'Making base of {pizza().name} pizza')
        self.pizza = pizza
        print('Base created successfully !')

    def toppings(self, topping: toppingPizza.Topping) -> None:
        self.pizza = topping(self.pizza)
        print(f'Adding {self.pizza.name} topping on pizza')
        print('Topping added successfully !')

    
if __name__ == "__main__":
    order = PizzaHut()
    order.basing(margheritaPizza.MargheritaPizza)
    # order.toppings(mushroom.Mushroom)
    order.toppings(extraCheese.ExtraCheese)
    print(f'Your final price is {order.pizza.cost()}')