# Исключения
class AddFuelValueError(ValueError):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"Добавляемое топливо в бак не может превышать 55 литров, а у вас {self.value}"


class СoefficientValueError(ValueError):
    def __init__(self, k):
        self.k = k

    def __str__(self):
        return f"Коэффициент трения колес по асфальту может быть равен 0.8 или 0.1, а у вас {self.k}"


class MaxrevolutionsValueError(ValueError):
    def __init__(self, max_revolutions):
        self.max_revolutions = max_revolutions

    def __str__(self):
        return f"Поставьте значение от 1000 до 10000"
