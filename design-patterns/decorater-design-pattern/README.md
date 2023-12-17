### Introduction:

Decorater Design Pattern is used to modify the functionality of an object at runtime. At the same time other instances of the same class will not be affected by this, so individual object gets the modified behavior.

In the sample usecase we have designed a custom pizza making & billing design in which a user can decide the base of the pizza & add as many toppings on it

#### Base Pizza:
    Farmhouse
    Mazerita 
    VegDelight

#### Decorater:
    Mushroom
    ExtraCheese
    Mozerlla

Sample Design would be:
```
// Adding Extracheese & Mushroom Topping on Base Farmhouse Pizza
ExtraCheese(Mushroom(Farmhouse))
```