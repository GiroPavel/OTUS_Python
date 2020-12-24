from abc import ABCMeta, abstractmethod

class BaseVehicleABC(metaclass=ABCMeta):

    @abstractmethod
    def way(self) -> str:  # пройдуный путь
        raise NotImplemented

    @abstractmethod
    def spend(self) -> str:  # расход топлива на 100 км
        raise NotImplemented


class BaseVehicle(BaseVehicleABC):

    def __init__(self, speed: int, time: int, way_go: int, fuel_spend: int, fuel=20):
        self.speed = speed
        self.time = time
        self.way_go = way_go
        self.fuel_spend = fuel_spend
        self.fuel = fuel

    def way(self) -> int:
        way = self.speed * self.time
        return way

    def spend(self) -> int:
        spend = float('{:.1f}'.format((self.fuel_spend / self.way_go) * 100))
        return spend

