from OTUS_Python.homework_2.Car import Car
from OTUS_Python.homework_2.MotorСar import MotorСar
from OTUS_Python.homework_2.Ship import Ship
from OTUS_Python.homework_2.MotorBoat import MotorBoat
from OTUS_Python.homework_2.Plane import Plane
from OTUS_Python.homework_2.Exceptions import AddFuelValueError, MaxrevolutionsValueError, СoefficientValueError

# Автомобиль
c = Car(120, 2, 317, 26.5)
print(c.makesound("Beep"))
print(f"Пройденый путь автомобиля равен {c.way()} километров")
print(f"Расход топлива на 100 км состовляет {c.spend()} литров")
print()
print("_______________________________________________________________")
# Поехали, в баке 20 литров
print(c.move(100))
print(c.move(100))
print(c.move(100))
print(c.move(100))
print(c.add_fuel(40))
print(c.move(100))
print()
print("_______________________________________________________________")
# Легковой автомобиль
m = MotorСar(120, 2, 317, 26.5)
e = m.engine(2, 4, 1000)
print(m.move(200))
print(m.add_tire_pressure(1))
print(m.stop(0.1, 80))
print()
print("_______________________________________________________________")
# Корабль
s = Ship(120, 2, 317, 26.5)
print(s.makesound("Beep-Beep"))
print(s.max_mass(3270, 170))
print()
print("_______________________________________________________________")
# Моторная лодка
ms = MotorBoat(120, 2, 317, 26.5)
print(ms.max_pass(48, 22, 10))
print()
print("_______________________________________________________________")
# Самолет
p = Plane(120, 2, 317, 26.5)
# Исключения
try:
    print(c.add_fuel(20))
except AddFuelValueError as e:
    print(f"Ошибка, введено неправильное значение: {e}")
    print()
else:
    print("Ошибки нет, введено правильное значение")
    print()


try:
    print(c.stop(0.1, 50))
except СoefficientValueError as c:
    print(f"Ошибка, введено неправильное значение: {c}")
else:
    print("Ошибки нет, введено правильное значение")


try:
    e = m.engine(2, 4, 11000)
except MaxrevolutionsValueError as m:
    print(f"Ошибка, введено неправильное значение: {m}")
else:
    print("Ошибки нет, введено правильное значение")