class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.__income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)
        self.__income = {'wage': wage, 'bonus': bonus}

    def get_full_name(self):
        return f'Полное имя: {self.name} {self.surname}'

    def get_total_income(self):
        return f'Доход с учетом премии: {self.__income["wage"] + self.__income["bonus"]} рублей'


worker = Position('Artur', 'Pirozhkov', 'driver', 40000, 20000)

print(worker.get_full_name())
print(worker.get_total_income())
