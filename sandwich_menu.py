import sys

from PyQt5.QtWidgets import QApplication

from Car.SandwichBuilderPattern.Customer import Customer
from Car.SandwichBuilderPattern.Food_Item_Types import Food_Item_Types
from TemperatureConverter.Dialog import Dialog


class Sandwich_Menu:
    app = QApplication(sys.argv)

    def __init__(self):
        self.user_choice_for_bread = None
        self.user_choice_for_meat = None
        self.user_choice_for_cheese = None
        self.user_choice_for_veggie_toppings = None
        self.user_choice_for_sauce = None
        self.customer = Customer()

    def display_welcome(self):
        Dialog.abdulmalik_message_display("WELCOME TO SEMICOLON SNACKS!!!")
        self.collect_customer_name()

    def collect_customer_name(self):
        customer_name, ok_pressed = Dialog.abdulmalik_input_str("""
        what is your name:_______________
        Enter any character with length less than 3 to go back""", "Customers name")
        if ok_pressed & isinstance(customer_name, str) :
            self.ask_customer_whether_they_want_to_make_sandwich(customer_name)
            return customer_name

        # else:len(customer_name) > 2
        #     user_input = Dialog.abdulmalik_input_str(customer_name + """
        #     would you like to go back
        #     yes ==> back
        #     no ==> exit""", "Prompt")
        #     if user_input == "yes":
        #         self.display_welcome()
        #     if user_input == "no":
        #         sys.exit(0)

    def ask_customer_whether_they_want_to_make_sandwich(self, customer_name):
        prompt = Dialog.abdulmalik_input_str(customer_name + " would you like to make a Sandwich(yes/no)", "Prompt")
        if prompt == "yes":
            self.main_menu()
        elif prompt == "no":
            user_input, ok_pressed = Dialog.abdulmalik_input_str(customer_name + " would you like to go back(yes/no)", "Prompt")
            if ok_pressed and user_input == "yes" and isinstance(user_input, int):
                self.display_welcome()

            elif user_input == "no":
                Dialog.abdulmalik_message_display("I think you want to continue")
                self.ask_customer_whether_they_want_to_make_sandwich(customer_name)

            else:
                Dialog.abdulmalik_message_display("I think you want to quit Bye for now")
                sys.exit()

    def main_menu(self):
        main_menu = """
        we have a variety of sandwich ingredients and they have different types
        which are according to your taste:
        1.) Bread
        2.) Meat
        3.) Cheese
        4.) Veggie toppings
        5.) Sauce
        6.) OK ==> Continue
        """
        user_input = Dialog.abdulmalik_input_str(main_menu, "Food Menu")
        if 'user_input.lower() == "0k"':
            self.prompt_customers_to_pick_bread_type()
            self.prompt_customers_to_pick_meat_type()
            self.prompt_customers_to_pick_cheese_type()
            self.prompt_customers_to_pick_veggie_toppings_type()
            self.prompt_customers_to_pick_sauce_type()
            self.make_sandwich()

    def prompt_customers_to_pick_bread_type(self):
        bread_type_menu = """
        We also have a variety of bread
        Enter
        1 --> Wheat Bread
        2 --> White Bread
        3 --> Sourdough"""
        user_input = Dialog.abdulmalik_input_str(bread_type_menu, "Bread Type Dialog")

        match user_input[0]:
            case 1:
                self.loop_through_food_item_types("wheat_bread")
            case 2:
                self.loop_through_food_item_types("white_bread")
            case 3:
                self.loop_through_food_item_types("sourdough")
            case _:
                self.ask_user_if_they_want_to_go_back()

    def prompt_customers_to_pick_meat_type(self):
        meat_type_menu = """
                We also have a variety of Meats for sandwich
                Enter
                1 --> Turkey
                2 --> Ham
                3 --> Roast Beef"""
        user_input = Dialog.abdulmalik_input_str(meat_type_menu, "Meat Type Dialog")

        match user_input[0]:
            case 1:
                self.loop_through_food_item_types("turkey")
            case 2:
                self.loop_through_food_item_types("ham")
            case 3:
                self.loop_through_food_item_types("roast_beef")
            case _:
                self.ask_user_if_they_want_to_go_back()

    def prompt_customers_to_pick_cheese_type(self):
        cheese_type_menu = """
                We also have a variety of Cheese for Sandwich
                Enter
                1 --> Cheddar
                2 --> Swiss
                3 --> Pepper Jack"""
        user_input = Dialog.abdulmalik_input_str(cheese_type_menu, "Cheese Type Dialog")

        match user_input[0]:
            case 1:
                self.loop_through_food_item_types("cheddar")
            case 2:
                self.loop_through_food_item_types("swiss")
            case 3:
                self.loop_through_food_item_types("pepper_jack")
            case _:
                self.ask_user_if_they_want_to_go_back()

    def prompt_customers_to_pick_veggie_toppings_type(self):
        veggie_toppings_type_menu = """
                We also have a variety of bread
                Enter
                1 --> Lettuce
                2 --> Tomato
                3 --> Onion"""
        user_input = Dialog.abdulmalik_input_str(veggie_toppings_type_menu, "Veggie Toppings Type Dialog")

        match user_input[0]:
            case 1:
                self.loop_through_food_item_types("lettuce")
            case 2:
                self.loop_through_food_item_types("tomato")
            case 3:
                self.loop_through_food_item_types("onion")
            case _:
                self.ask_user_if_they_want_to_go_back()

    def prompt_customers_to_pick_sauce_type(self):
        sauce_type_menu = """
                We also have a variety of Sauces for Sandwich
                Enter
                1 --> Mayonnaise
                2 --> Ketchup
                3 --> Mustard"""
        user_input = Dialog.abdulmalik_input_str(sauce_type_menu, "Sauce Type Dialog")

        match user_input[0]:
            case 1:
                self.loop_through_food_item_types("mayonnaise")
            case 2:
                self.loop_through_food_item_types("ketchup")
            case 3:
                self.loop_through_food_item_types("mustard")
            case _:
                self.ask_user_if_they_want_to_go_back()

    def loop_through_food_item_types(self, food_type):
        food_item_types = [Food_Item_Types.BREAD_TYPE, Food_Item_Types.MEAT_TYPE, Food_Item_Types.CHEESE_TYPE,
                           Food_Item_Types.VEGGIE_TOPPINGS_TYPE, Food_Item_Types.SAUCE_TYPE]
        for food in food_item_types:
            for food_types in food.item_type:
                if food_types == food_type:
                    self.loop_through_bread(food_types)
                    self.loop_through_meat(food_types)
                    self.loop_through_cheese(food_types)
                    self.loop_through_veggie_toppings(food_types)
                    self.loop_through_sauce(food_types)

    def ask_user_if_they_want_to_go_back(self):
        prompt = Dialog.abdulmalik_input_str(" would you like to go back(yes/no)", "Prompt")
        if prompt == "yes":
            self.main_menu()
        elif prompt == "no":
            user_input = Dialog.abdulmalik_input_str(
                self.collect_customer_name() + " would you like to go to start again(yes/no)", "Prompt")
            if user_input == "yes":
                self.display_welcome()

            elif user_input == "no":
                Dialog.abdulmalik_message_display("I think you don't want to continue")
                sys.exit(0)

    def loop_through_bread(self, food_types):
        for _ in Food_Item_Types.BREAD_TYPE:
            if food_types in Food_Item_Types.BREAD_TYPE:
                self.user_choice_for_bread = food_types

    def loop_through_meat(self, food_types):
        for _ in Food_Item_Types.MEAT_TYPE:
            if food_types in Food_Item_Types.MEAT_TYPE:
                self.user_choice_for_meat = food_types

    def loop_through_cheese(self, food_types):
        for _ in Food_Item_Types.CHEESE_TYPE:
            if food_types in Food_Item_Types.CHEESE_TYPE:
                self.user_choice_for_cheese = food_types

    def loop_through_veggie_toppings(self, food_types):
        for _ in Food_Item_Types.VEGGIE_TOPPINGS_TYPE:
            if food_types in Food_Item_Types.VEGGIE_TOPPINGS_TYPE:
                self.user_choice_for_veggie_toppings = food_types

    def loop_through_sauce(self, food_types):
        for _ in Food_Item_Types.SAUCE_TYPE:
            if food_types in Food_Item_Types.SAUCE_TYPE:
                self.user_choice_for_sauce = food_types

    def make_sandwich(self):
        self.customer.make_sandwich(self.user_choice_for_bread, self.user_choice_for_meat, self.user_choice_for_cheese,
                                    self.user_choice_for_veggie_toppings, self.user_choice_for_sauce)
