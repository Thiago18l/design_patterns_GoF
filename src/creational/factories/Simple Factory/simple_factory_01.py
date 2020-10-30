"""
In OOP programming, the term factory refers to a class or method
who is responsible for creating objects.
Benefits:
    Allow to create a system with low coupling between classes because
    hide as classes that create client code objects.
    Facilitate the addition of new classes to the code, because the client does not
    neither knows nor uses the class implementation (uses a factory).
    They can facilitate the process of "caching" or creating "singletons" because the
    factory can return an object already created to the customer, when trying to create
    new objects whenever the customer needs.
Disadvantages:
    Can introduce many classes without code
Let's see 2 types of Factory from GoF: Factory method and Abstract Factory
In this class:
Simple Factory <- A kind of parameterized Factory Method
Simple Factory cannot be considered a design pattern by itself
Simple Factory can break SOLID principles

"""

from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def seek_client(self) -> None: pass

class ExpensiveCar(Vehicle):
    def seek_client(self) -> None:
        print("Car expensive is getting the client")

class PopularCar(Vehicle):
    def seek_client(self) -> None:
        print("popular car is getting the client")
    
class ExpensiveMotorcycle(Vehicle):
    def seek_client(self) -> None:
        print("Expensive motorcycle is getting the client")

class PopularMotorcycle(Vehicle):
    def seek_client(self) -> None:
        print("Popular motorcycle is getting the client")
        

class FactoryVehicle:
    @staticmethod
    def get_car(type: str) -> Vehicle:
        if type == 'expensiveCar':
            return ExpensiveCar()
        if type == 'popularCar':
            return PopularCar()
        if type == 'expensiveMotorcycle':
            return ExpensiveMotorcycle()
        if type == 'popularMotorcycle':
            return PopularMotorcycle()
        assert 0, 'vehicle does not exist'

if __name__ == "__main__":
    from random import choice
    available_vehicles = ['expensiveCar', 'popularCar', 'expensiveMotorcycle', 'popularMotorcycle']
    
    for i in range(10):
        car = FactoryVehicle.get_car(choice(available_vehicles))
        car.seek_client()
