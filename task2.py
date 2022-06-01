class ZeroDivision(Exception):
    def __init__(self):
        self.first_number = int(input('Введите делимое: '))
        self.second_number = int(input('Введите делитель: '))
        if self.second_number == 0:
            self.message = 'Ошибка: деление на 0'
        else:
            self.message = f'{self.first_number}/{self.second_number} = ' \
                           f'{self.first_number / self.second_number}'
        super().__init__(self.message)

    def __str__(self):
        return self.message


example = ZeroDivision
print(example())
