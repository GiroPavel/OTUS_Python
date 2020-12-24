from Car import Car
from Exceptions import MaxrevolutionsValueError
from dataclasses import dataclass

class MotorСar(Car):  # Легковой автомобиль
    WHEELS = 4  # количество колес 4 шт
    WEIGHT = 2  # вес автомобиля 2 тонны
    LIFTING = 300  # грузоподъемность 300 кг
    LENGHT = 2  # длинна легкового автомобиля 2 метра
    TIRE_PRESSURE = 2.2  # давление шин


    def move(self, dist, fuel_consumption=6):
        res = super().move(dist)
        dist_to_station = (res * 100) // fuel_consumption
        print(f"Топлива хватит на {dist_to_station} киллометра")
        return dist_to_station

    # Подкачать шины
    def add_tire_pressure(self, value, tire_pressure=1.5):
        self.tire_pressure = tire_pressure
        tire_pressure += value

        if tire_pressure == self.TIRE_PRESSURE:
            print("Давление шин в норме")
        elif tire_pressure > self.TIRE_PRESSURE:
            print("Давление шин выше нормы")
        else:
            print("Давление шин ниже нормы")
        return tire_pressure

    # Обороты двигателя
    @dataclass
    class Engine:
        liters: int
        number_of_pistons: int
        max_revolutions: int

        def __post_init__(self):
            if 2500 <= self.max_revolutions <= 6000:
                print(f"Нормальная работа двигателя, количество оборотов равно {self.max_revolutions}")
            elif 1000 <= self.max_revolutions <= 2500:
                print(f"Двигатель работает на холостом ходу, количество оборотов равно {self.max_revolutions}")
            elif 6000 <= self.max_revolutions <= 10_000:
                print(f"Двигатель работает на максимуме, количество оборотов равно {self.max_revolutions}")
            else:
                raise MaxrevolutionsValueError(self.max_revolutions)