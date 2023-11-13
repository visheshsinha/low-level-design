#### Observer Design Pattern

In observer design pattern we have two objects - 
1. `Observer`
2. `Observable`

Whenever there is a state change in the `Observable` object, the object updates all the `Observer` objects observing it.

`Observer` objects later does thier function based on the updates.


#### Implementation:


1. ObservableInterface, this has

```
observerInterfaces = []

add(ObserverInterface Obj) - registration
remove(ObserverInterface Obj)
notify() {
    // notifies all observerInterfaces
}
setData()
```

2. ObserverInterface, this has

```
update()
```

One Observable Object can be Observed by many Observer Objects , so its `one to many` relationship.


3. ObservableConcreteClass, this has

```
add(ObserverInterface Obj) {
    observerInterfaces.append(Obj)
}

remove(ObserverInterface Obj) {
    observerInterfaces.remove(Obj)
}

notify() {
    # Iterate and notify / update state - Obj.update()
}

setData(change) {
    data = change
    notify()
}
```

4. ObserverConcreteClass, this has

```
update() {
    // make ObservableConcreteClass object and use as a constructor injection inorder to have the instance check herein
}
```


#### Walmart Low Level Design Round 2022 Interview Question:

#### Problem Statement - 

Suppose there is a product on the marketplace which is out of stock. And the market place gives an option of 'NOTIFY ME', we have to inform all the users who clicked notify me once the product is back in stock.

- Solution Coded in subfolders