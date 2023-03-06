from Car.SandwichBuilderPattern.Sandwich_Machine import Sandwich_Machine


class Customer:

    def __init__(self):
        self.machine = Sandwich_Machine()

    def make_sandwich(self, bread, meat, cheese, veggie_toppings, sauce):
        self.machine.set_sandwich_bread(bread)
        self.machine.set_sandwich_meat(meat)
        self.machine.set_sandwich_cheese(cheese)
        self.machine.set_sandwich_veggie_toppings(veggie_toppings)
        self.machine.set_sandwich_sauce(sauce)
        return self.machine.sandwich

    def __str__(self):
        return "%s, \n%s, %s, \n%s" % ("{", "Machine: ", self.machine, "}")
    