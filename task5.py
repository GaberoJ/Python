class Stationery:
    title = 'Stationery'

    def draw(self):
        return 'Запуск отрисовки'


class Pen(Stationery):
    def draw(self):
        return 'Я написан ручкой'


class Pencil(Stationery):
    def draw(self):
        return 'Я написан карандашом'


class Handle(Stationery):
    def draw(self):
        return 'Я написан маркером'


example = Stationery()
example_pen = Pen()
example_pencil = Pencil()
example_handle = Handle()


print(example.draw())
print(example_pen.draw())
print(example_pencil.draw())
print(example_handle.draw())
