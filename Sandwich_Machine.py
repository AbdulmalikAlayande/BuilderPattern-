from Car.SandwichBuilderPattern.Sandwich import Sandwich


class Sandwich_Machine:

    def __init__(self):
        self.sandwich = Sandwich()

    def set_sandwich_bread(self, bread_type):
        self.sandwich.bread = bread_type

    def get_sandwich_bread(self):
        return self.sandwich.bread

    def set_sandwich_meat(self, meat_type):
        self.sandwich.meat = meat_type

    def get_sandwich_meat(self):
        return self.sandwich.meat

    def set_sandwich_cheese(self, cheese_type):
        self.sandwich.cheese = cheese_type

    def get_sandwich_cheese(self):
        return self.sandwich.cheese

    def set_sandwich_veggie_toppings(self, veggie_toppings_type):
        self.sandwich.veggie_toppings = veggie_toppings_type

    def get_sandwich_veggie_toppings(self):
        return self.sandwich.veggie_toppings

    def set_sandwich_sauce(self, sauce_type):
        self.sandwich.sauce = sauce_type

    def get_sandwich_sauce(self):
        return self.sandwich.sauce

    def __str__(self):
        return "%s,\n%s, %s, \n%s, %s, \n%s, %s, \n%s, %s, \n%s, %s, \n%s" % ("{", "Bread: ", self.get_sandwich_bread(), "Meat: ", self.get_sandwich_meat(),
                                                                              "Cheese:",self.get_sandwich_cheese(), "Veggie Toppings: ", self.get_sandwich_veggie_toppings(),
                                                                              "Sauce: ", self.get_sandwich_sauce(), "}")
