from Car.BuilderPattern.Car_Builder import Car_Builder


class Car_Director:

    def __init__(self, builder: Car_Builder):
        self._builder = builder

    def build_car(self):
        self._builder.set_car_wheels(number_of_wheels=8)
        self._builder.set_car_Engine(engine_horse_power=200)
        self._builder.set_car_color(color="blue")
        return self._builder.get_car


mechanic = Car_Builder()
engineer = Car_Director(mechanic)
car = engineer.build_car()
print(car.get_car_color)
