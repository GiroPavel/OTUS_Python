from OTUS_Python.homework_2.Ship import Ship

class MotorBoat(Ship):  # Моторная лодка
    WEIGHT = 4000  # максимальный вес для моторных лодок 4 тонны
    LIFTING = 500  # грузоподъемность 500 кг
    DIS = 17  # вдоизмещение корабля 17 тон
    LENGHT = 20  # длинна парусной лодки 20 метров
    MAX_FUEL = 500  # максимальный объем бака 500 литров

    # Расчет массы поссажиров допускаемых в моторную лодку
    def max_pass(self, mm, mt, mb, v=3270, vm=170):
        """
        :param mm: - масса подвесного мотора
        :param mt: - масса бензобака
        :param mb: - масса стартерной батареи
        :param v:  - объем корпуса
        :param vm: - масса корпуса
        :return:
        """
        res = super().max_mass(v, vm)
        max_p = res - (mm + mt + mb)
        print(f"Масса пассажиров, допускаемых к посадке в моторную лодку равна {max_p} килограмм")
        return max_p