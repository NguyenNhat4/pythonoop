"""
Bài tập: Cây kế thừa phương tiện (mức khá)
- Base Vehicle(make) với method move() -> str (raise NotImplementedError)
- Car(Vehicle): move() -> "drive"
- Bike(Vehicle): move() -> "pedal"
- ElectricCar(Car): thêm battery_kwh, move() -> "drive-electric"
"""


class Vehicle:
    def __init__(self, make: str) -> None:
        # TODO: validate make
        raise NotImplementedError

    def move(self) -> str:
        raise NotImplementedError


class Car(Vehicle):
    def move(self) -> str:
        # TODO
        raise NotImplementedError


class Bike(Vehicle):
    def move(self) -> str:
        # TODO
        raise NotImplementedError


class ElectricCar(Car):
    def __init__(self, make: str, battery_kwh: int) -> None:
        # TODO: super().__init__ và validate
        raise NotImplementedError

    def move(self) -> str:
        # TODO
        raise NotImplementedError
