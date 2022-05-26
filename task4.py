class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return 'Едем вперед'

    def stop(self):
        return 'Остановочка'

    def turn(self, direction):
        return f'Повернули {direction}'

    def show_speed(self):
        return f'Текущая скорость: {self.speed}'


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            message = 'Превышаем??'
        else:
            message = f'Ваша скорость: {self.speed}, It`s ok'
        return message


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            message = 'Превышаем??'
        else:
            message = f'Ваша скорость: {self.speed}, It`s ok'
        return message


class PoliceCar(Car):
    def show_speed(self):
        if self.speed > 90:
            message = 'В полиции так не гоняют'
        else:
            message = f'Ваша скорость: {self.speed}, It`s ok'
        return message


first_car = TownCar(61, 'blue', 'BMW')
second_car = WorkCar(35, 'green', 'Volvo')
third_car = PoliceCar(123, 'white', 'Skoda', True)

print(first_car.show_speed())
print(second_car.show_speed())
print(third_car.show_speed())
