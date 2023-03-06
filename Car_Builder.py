from Car.BuilderPattern.Car import Car


class Car_Builder:
    def __init__(self):
        self._car = Car()

    def set_car_wheels(self, number_of_wheels: int) -> None:
        self._car.number_Of_wheel = number_of_wheels

    def get_car_wheels(self) -> int:
        return self._car.number_Of_wheel

    def set_car_Engine(self, engine_horse_power: int) -> None:
        self._car.engine = engine_horse_power

    def get_car_Engine(self) -> int:
        return self._car.engine

    def set_car_color(self, color: str) -> None:
        self._car.car_color = color

    def get_car_color(self) -> str:
        return self._car.car_color

    def get_car(self) -> Car():
        return self._car
