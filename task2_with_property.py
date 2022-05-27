class Clothes:
    sum_of_materials = 0

    def __init__(self, value):
        self.parameter = value

    @property
    def calculation_coat(self):
        result = self.parameter / 6.5 + 0.5
        Clothes.sum_of_materials += result
        return result

    @property
    def calculation_suit(self):
        result = 2 * self.parameter + 0.3
        Clothes.sum_of_materials += result
        return result


suit_example = Clothes(2)
suit_example1 = Clothes(4)
coat_example = Clothes(42)
coat_example1 = Clothes(45)

print(suit_example.calculation_suit)
print(suit_example1.calculation_suit)
print(coat_example.calculation_coat)
print(coat_example1.calculation_coat)
print(f'Суммарный расход ткани: {Clothes.sum_of_materials}')


