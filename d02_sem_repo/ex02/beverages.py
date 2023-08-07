class HotBeverage:
    def __init__(self, price = 0.30, name = "hot beverage"):
        self.price = price
        self.name = name

    def description(self):
        return("Just some hot water in a cup.")
    
    def __str__(self):
        return ("name : " + self.name + "\n" + 
                "price : " + str(self.price) + "\n" + 
                "description : " + self.description()
                )

class Coffee(HotBeverage):
    def __init__(self):
        super().__init__(0.40, "coffee")

    def description(self):
        return "A coffee, to stay awake."
    
class Tea(HotBeverage):
    def __init__(self):
        super().__init__(0.30, "tea")
    
class Chocolate(HotBeverage):
    def __init__(self):
        super().__init__(0.50, "chocolate")

    def description(self):
        return "Chocolate, sweet chocolate..."
    
class Cappuccino(HotBeverage):
    def __init__(self):
        super().__init__(0.45, "cappuccino")

    def description(self):
        return "Un po’ di Italia nella sua tazza!"


if __name__ == "__main__":
    hot_beverage = HotBeverage()
    print(hot_beverage)

    coffee = Coffee()
    print(coffee)

    tea = Tea()
    print(tea)

    chocolate = Chocolate()
    print(chocolate)

    cappuccino = Cappuccino()
    print(cappuccino)

    