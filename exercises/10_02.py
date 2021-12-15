#!/usr/bin/env python3
class Car:
    def __init__(self, name: str, sound: str) -> None:
        self.name = name
        self.sound = sound

    def drive(self):
        print(self.sound)


class ElectricCar(Car):
    def __init__(self, name: str):
        sound = "bzzzzzzzz..."
        super().__init__(name, sound)


class SportsCar(Car):
    def __init__(self, name: str):
        sound = "VROOAAAAAARR!!!"
        super().__init__(name, sound)


ec = ElectricCar("Prius")
sc = SportsCar("Ferrari")

ec.drive()
sc.drive()
