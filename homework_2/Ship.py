from OTUS_Python.homework_2.BaseVehicles import BaseVehicle

class Ship(BaseVehicle): # Корабль
    DIS = 5000  # водоизмещение

    # Расчет максимально допустимой нагрузки
    def max_mass(self, v, vm):
        """
        :param v: - объем корпуса
        :param vm: - масса корпуса
        :return:
        """
        max_m = 1 / 5 * (v - vm)
        print(f"Максимально допустимая нагрузка равна {max_m} килограмм")
        return max_m