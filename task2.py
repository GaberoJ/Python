class Road:
    def __init__(self, lenght, width, k1, k2):
        self._lenght = lenght
        self._width = width
        self.k1 = k1
        self.k2 = k2

    def mass_of_covering(self):
        result = self._lenght * self._width * self.k1 * self.k2
        return f'{self._lenght}м * {self._width}м * {self.k1}кг * {self.k2}см = {result // 1000} т.'


street = Road(5000, 20, 25, 5)
print(street.mass_of_covering())

street1 = Road(1000, 15, 25, 5)
print(street1.mass_of_covering())
