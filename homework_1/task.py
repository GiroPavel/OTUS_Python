from time import time
from functools import partial
from functools import wraps

n = range(11)

print("Список целых чисел:", list(n))

LEVEL = 0 # int
def trace(func):
    @wraps(func)
    def wrapper(*args):
        global LEVEL
        l = "--> " * LEVEL # str
        name = func.__name__
        print(l + ("%s%s" % (name, args)))
        LEVEL += 1
        res = func(*args)
        LEVEL -= 1
        print(l + ("%s" % res))
        return res
    return wrapper

def timing_dec(func):
    @wraps(func)
    def wrapper(*args):
        start_time = time()
        res = func(*args)
        end_time = time()
        print("Время выполнения функции 'power_n':", end_time - start_time)
        return res
    return wrapper

# 1
def power (a, p=int(input("Введите степень:"))):
    return a ** p

@timing_dec
def power_n():
    res = map(power, n)
    return res
# 2
def power_part_n():
    res = map(partial(pow, exp=2), n)
    return res

def only_even():
    res = filter(lambda n: n % 2 == 0, n)
    return res

def only_odd():
    res = filter(lambda n: n % 2 != 0, n)
    return res

def prime(number):
    primes = []
    for pr in range(2, number):
        isPrime = True
        for i in range(2, pr):
            if pr % i == 0:
                isPrime = False
                break
        if isPrime:
            primes.append(pr)
    return primes

@trace
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

print("Список квадратов целых чисел:", list(power_n()))
print("Список квадратов с использованием 'Partial':", list(power_part_n()))
print("Только четные числа:", list(only_even()))
print("Только нечетные числа:", list(only_odd()))
print("Простые числа в диапазоне от '0 до 10':", prime(11))
print()
print("Вложенные входы в функцию на примере чисел Фибаначчи:")
print("Список чисел Фибаначчи:", [fib(n) for n in range(5)])








