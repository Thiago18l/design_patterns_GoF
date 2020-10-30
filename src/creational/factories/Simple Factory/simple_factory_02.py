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
    def __init__(self, type: str) -> None:
        self.carro = self.get_car(type)
    
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
        
    def catch_client(self) -> None:
        self.carro.seek_client()


if __name__ == "__main__":
    from random import choice
    available_vehicles = ['expensiveCar', 'popularCar',
                          'expensiveMotorcycle', 'popularMotorcycle']

    for i in range(10):
        car = FactoryVehicle(choice(available_vehicles))
        car.catch_client()
