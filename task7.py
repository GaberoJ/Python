class Complex:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        if self.b == -other.b:
            return f'Сумма чисел: ({self.a} + {self.b}i) + ({other.a} + {other.b}i) = ' \
                   f'\033[32m{self.a + other.a}\033[38m'
        else:
            result = f'Сумма чисел: ({self.a} + {self.b}i) + ({other.a} + {other.b}i) = \033[32m{self.a + other.a} + ' \
                     f'{self.b + other.b}i\033[38m'
            result_str = result.replace('+ -', '- ')
            return result_str

    def __mul__(self, other):
        result = f'Произведение чисел: ({self.a} + {self.b}i) * ({other.a} + {other.b}i) = {self.a * other.a} + ' \
                 f'{self.a * other.b}i + {self.b * other.a}i + {self.b * other.b}i^2 = \033[32m' \
                 f'{self.a * other.a -(self.b * other.b)} + {self.a * other.b + self.b * other.a}i \033[38m'
        result_str = result.replace('+ -', '- ')
        return result_str

    def __str__(self):
        result = f'Число: {self.a} + {self.b}i'
        result_str = result.replace('+ -', '- ')
        return result_str


first_number = Complex(4, -8)
second_number = Complex(5, 2)
third_number = Complex(-7, 5)

print(first_number + second_number)
print(second_number + third_number)
print(first_number + third_number)
print()
print(first_number * second_number)
print(second_number * third_number)
print(first_number * third_number)
