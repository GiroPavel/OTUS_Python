from abc import ABCMeta, abstractmethod

class BaseVehicleABC(metaclass=ABCMeta):

    @abstractmethod
    def way(self) -> int:  # пройдуный путь
        raise NotImplemented

    @abstractmethod
    def spend(self) -> int:  # расход топлива на 100 км
        raise NotImplemented

    @abstractmethod
    def makesound(self, text) -> str:  # издать звук
        raise NotImplemented

class BaseVehicle(BaseVehicleABC):
    # Общие свойсва и методы для всех средств передвижения
    WEIGHT = int  # вес
    LIFTING = int  # грузоподъемность
    SOUND = str  # издать звук

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

    def makesound(self, text) -> str:
        self.SOUND = text
        if text == "Beep":
            print("У вас автомобиль")
        elif text == "Beep-Beep":
            print("У вас корабль")
        elif text == "Beep-Beep-Beep":
            print("У вас самолет")
        else:
            print("ХМ, что у вас")
        return text
