class Food_Item_Types:

    BREAD_TYPE = ["wheat_bread", "white_bread", "sourdough"]
    MEAT_TYPE = ["turkey", "ham", "roast_beef"]
    CHEESE_TYPE = ["cheddar", "swiss", "pepper_jack"]
    VEGGIE_TOPPINGS_TYPE = ["lettuce", "tomato", "onion"]
    SAUCE_TYPE = ["mayonnaise", "ketchup", "mustard"]

    def __init__(self, *item_types: str) -> None:
        self.food_item_types = item_types

    def get_item_type(self) -> list[str]:
        empty_list = []
        for item in self.food_item_types:
            empty_list.append(item)
        return empty_list

    def __str__(self):
        return f"""
        {self.BREAD_TYPE}
        {self.MEAT_TYPE}
        """

