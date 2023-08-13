Decorator design pattern is something like adding extra feature on the top of the any existing feature to extends the functionality of object

Lets take an example of pizza

we have a some base pizza and if we want to add different types topping on top of base pizza we can do easily using decorator design

why we need decorator design pattern ?

To avoid class explosion if we have different topping and that we need to make combinations of using base class and toppings flavour then it would be difficult to make all child classes for each combinations



Keep in mind : after adding decorator on base object resulting object always should be base type object


In this Lets take example and code it
we will take 3 base pizza class Margherita, FarmHouse, VegLoaded
and topping class like ExtraCheese, Mushroom, Capsicum