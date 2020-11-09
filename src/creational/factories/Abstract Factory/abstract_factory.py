from abc import ABC, abstractmethod


class VehicleLuxous(ABC):
    @abstractmethod
    def seek_client(self) -> None: pass


class VehiclePopular(ABC):
    @abstractmethod
    def seek_client(self) -> None: pass


class ExpensiveCarZN(VehicleLuxous):
    def seek_client(self) -> None:
        print("Car expensive is getting the client in the ZN")


class PopularCarZN(VehiclePopular):
    def seek_client(self) -> None:
        print("popular car is getting the client in the ZN")


class ExpensiveCarZS(VehicleLuxous):
    def seek_client(self) -> None:
        print("Car expensive is getting the client in the ZS")


class PopularCarZS(VehiclePopular):
    def seek_client(self) -> None:
        print("popular car is getting the client in the ZS")


class VehicleFactory(ABC):
    @staticmethod
    @abstractmethod
    def get_car_expensive() -> VehicleLuxous: pass

    @staticmethod
    @abstractmethod
    def get_car_popular() -> VehiclePopular: pass


class ZoneNorthVehicleFactory(VehicleFactory):
    @staticmethod
    def get_car_expensive() -> VehicleLuxous:
        return ExpensiveCarZN()

    @staticmethod
    def get_car_popular() -> VehiclePopular:
        return PopularCarZN()


class ZoneSouthVehicleFactory(VehicleFactory):
    @staticmethod
    def get_car_expensive() -> VehicleLuxous:
        return ExpensiveCarZS()

    @staticmethod
    def get_car_popular() -> VehiclePopular:
        return PopularCarZS()


class Branches:
    @staticmethod
    def seek_client():
        for factory in [ZoneNorthVehicleFactory(), ZoneSouthVehicleFactory()]:
            popular_car = factory.get_car_popular()
            popular_car.seek_client()

            expensive_car = factory.get_car_expensive()
            expensive_car.seek_client()


if __name__ == "__main__":
    client = Branches()
    client.seek_client()



