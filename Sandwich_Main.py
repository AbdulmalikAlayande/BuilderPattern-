from Car.SandwichBuilderPattern.sandwich_menu import Sandwich_Menu


class Sandwich_Main:

    @staticmethod
    def main():
        sandwich_menu = Sandwich_Menu()
        sandwich_menu.display_welcome()
        sandwich_menu.main_menu()


if __name__ == '__main__':
    sandwich_main = Sandwich_Main()
    sandwich_main.main()
