class Pizza:

    pizzaPrices = {"small": 8, "medium": 10, "large": 12}

    def __init__(self, size):
        self.toppings = set()
        self.size = "small"
        if size.lower() in self.pizzaPrices:
            self.size = size.lower()

    def addTopping(self, topping):
        self.toppings.add(topping.lower())

    def removeTopping(self, topping):
        self.toppings.remove(topping.lower())

    def setSize(self, newSize):
        if newSize.lower() in self.pizzaPrices:
            self.size = newSize.lower()

    def getSize(self):
        return self.size

    def getPrice(self):
        return self.pizzaPrices[self.size]

    def getToppings(self):
        return self.toppings

    def __str__(self):
        output = f"{self.size} pizza with:"
        for topping in self.toppings:
            output += f"\n- {topping}"
        output += f"\nPrice: £{self.getPrice()}\n"
        return output


class Order:

    def __init__(self):
        self.pizzas = []

    def addPizza(self, pizza):
        self.pizzas.append(pizza)

    def getTotalPrice(self):
        totalPrice = 0
        for pizza in self.pizzas:
            totalPrice += pizza.getPrice()
        return totalPrice

    def __str__(self):
        output = "Your order contains:\n"
        for pizza in self.pizzas:
            output += str(pizza)
        output += f"Total: £{self.getTotalPrice()}"
        return output


class StuffedCrustPizza(Pizza):
    
    crustTypes = ("cheese", "garlic", "hot dog")

    def __init__(self, size, crust):
        super().__init__(size)
        self.crust = "cheese"
        if crust.lower() in self.crustTypes:
            self.crust = crust.lower()

    def getCrust(self):
        return self.crust

    def setCrust(self, newCrust):
        if newCrust in self.crustTypes:
            self.crust = newCrust

    def getPrice(self):
        return super().getPrice() + 2

    def __str__(self):
        output = f"A {self.size} stuffed crust pizza with:"
        for topping in self.toppings:
            output += f"\n- {topping}"
        output += f"\nCrust type: {self.crust}"
        output += f"\nPrice: £{self.getPrice()}\n"
        return output


def test():
    myOrder = Order()
    pizza1 = Pizza("small")
    pizza1.addTopping("Pepperoni")
    pizza1.addTopping("Jalapenos")
    pizza1.setSize("large")

    pizza2 = StuffedCrustPizza("Medium", "Cheese")
    pizza2.addTopping("Ham")
    pizza2.addTopping("Mushrooms")
    pizza2.setCrust("Garlic")

    myOrder.addPizza(pizza1)
    myOrder.addPizza(pizza2)

    print(myOrder)