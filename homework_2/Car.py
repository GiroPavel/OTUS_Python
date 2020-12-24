from BaseVehicles import BaseVehicle
from Exceptions import AddFuelValueError, СoefficientValueError

class Car(BaseVehicle):  # Автомобиль
    WHEELS = 4
    MAX_FUEL = 55

    # Тормозной путь для всех автомобилей
    def stop(self, k, speed_c):
        if k == 0.8:
            s = (speed_c ** 2) / (250 * k)
            print(f"Тормозной путь, при скорости {speed_c}, по сухой дороге равен {s} метров")
        elif k == 0.1:
            s = (speed_c ** 2) / (250 * k)
            print(f"Тормозной путь, при скорости {speed_c}, по льду равен {s} метров")
        else:
            raise СoefficientValueError(k)
        return s

    # Поехали
    def move(self, dist, fuel_consumption=6):  # fuel_consumption - потребление на 100км
        # self.fuel = fuel
        fuel_to_spend = (dist * fuel_consumption) // 100
        # print(fuel_to_spend)
        if fuel_to_spend > self.fuel:
            print(f"Не достаточно топлива, заправьтесь, в баке всего {self.fuel} литров")
        else:
            self.fuel -= fuel_to_spend
            # print(self.fuel)
            print(f"Вы проехали {dist} километров, потратили {fuel_to_spend} литров, осталось {self.fuel} литра")
        return self.fuel

    # Зальем топлива
    def add_fuel(self, value):
        print(f"Добавили {value} литров топлива")
        self.fuel += value
        if self.fuel > self.MAX_FUEL:
            raise AddFuelValueError(self.fuel)
        print(f"В баке {self.fuel} литра")
        return self.fuel