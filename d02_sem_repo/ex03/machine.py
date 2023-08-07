from beverages import HotBeverage, Coffee, Tea, Chocolate, Cappuccino
import random

class CoffeeMachine:
    def __init__(self):
        self.servedDrinks = 0
        self.repaired = False

    class EmptyCup(HotBeverage):
        def __init__(self):
            super().__init__(0.90, "empty cup")

        def description(self):
            return "An empty cup?! Gimme my money back!"
    
    class BrokenMachineException(Exception):
        def __init__(self, message="This coffee machine has to be repaired."):
            super().__init__(message)

    def repair(self):
        self.servedDrinks = 0
        repaired = True
    
    def serve(self, hotBeverage):
        if self.servedDrinks >= 10:
            self.repaired = False
            raise CoffeeMachine.BrokenMachineException()
        
        self.servedDrinks += 1

        if random.choice([True, False]):
            return CoffeeMachine.EmptyCup()
        else:
            return hotBeverage()

if __name__ == "__main__":
    coffeeMachine = CoffeeMachine()

    try:
        drink = coffeeMachine.serve(Coffee)
        print(drink, "\n")
        drink = coffeeMachine.serve(Tea)
        print(drink, "\n")
        drink = coffeeMachine.serve(Chocolate)
        print(drink, "\n")
        drink = coffeeMachine.serve(Cappuccino)
        print(drink, "\n")
        drink = coffeeMachine.serve(Coffee)
        print(drink, "\n")
        drink = coffeeMachine.serve(Tea)
        print(drink, "\n")
        drink = coffeeMachine.serve(Chocolate)
        print(drink, "\n")
        drink = coffeeMachine.serve(Cappuccino)
        print(drink, "\n")
        drink = coffeeMachine.serve(Coffee)
        print(drink, "\n")
        drink = coffeeMachine.serve(Tea)
        print(drink, "\n")
        drink = coffeeMachine.serve(Cappuccino)
        print(drink, "\n")
    except Exception as e:
        print("Description error:", str(e))

    coffeeMachine.repair()
    print("\n\nCoffee machine repaired.\n\n")

    try:
        drink = coffeeMachine.serve(Coffee)
        print(drink, "\n")
        drink = coffeeMachine.serve(Tea)
        print(drink, "\n")
        drink = coffeeMachine.serve(Chocolate)
        print(drink, "\n")
        drink = coffeeMachine.serve(Cappuccino)
        print(drink, "\n")
        drink = coffeeMachine.serve(Coffee)
        print(drink, "\n")
        drink = coffeeMachine.serve(Tea)
        print(drink, "\n")
        drink = coffeeMachine.serve(Chocolate)
        print(drink, "\n")
        drink = coffeeMachine.serve(Cappuccino)
        print(drink, "\n")
        drink = coffeeMachine.serve(Coffee)
        print(drink, "\n")
        drink = coffeeMachine.serve(Tea)
        print(drink, "\n")
        drink = coffeeMachine.serve(Cappuccino)
        print(drink, "\n")
    except Exception as e:
        print("Description error:", str(e))