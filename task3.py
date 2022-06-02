class Cell:
    def __init__(self, number_of_cells):
        self.number_of_cells = number_of_cells

    def __add__(self, other):
        return Cell(self.number_of_cells + other.number_of_cells)

    def __sub__(self, other):
        if self.number_of_cells > other.number_of_cells:
            return Cell(self.number_of_cells - other.number_of_cells)
        else:
            raise ValueError('Невозможно произвести вычитание')

    def __mul__(self, other):
        return Cell(self.number_of_cells * other.number_of_cells)

    def __floordiv__(self, other):
        return self.number_of_cells // other.number_of_cells

    def make_order(self, num_of_cells_in_row):
        if self.number_of_cells % num_of_cells_in_row == 0:
            result = f'{"*" * num_of_cells_in_row}\n' * (self.number_of_cells // num_of_cells_in_row)
            return result[:-1]
        else:
            result = f'{"*" * num_of_cells_in_row}\n' * ((self.number_of_cells // num_of_cells_in_row) + 1)
            return result[:-(num_of_cells_in_row - self.number_of_cells % num_of_cells_in_row + 1)]

    def __str__(self):
        return str(self.number_of_cells)


first_cell = Cell(12)
second_cell = Cell(7)
addition = first_cell + second_cell
subtraction = first_cell - second_cell
multiplication = first_cell * second_cell
division = first_cell // second_cell
example = first_cell + second_cell

print(f'Сложение: {addition}')
print(f'Вычитание: {subtraction}')
print(f'умножение: {multiplication}')
print(f'Деление: {division}')
print(f'\nПример: {example}')
print(f'Разделение по ячейкам:\n{example.make_order(8)}')
print(f'Разделение по ячейкам:\n{example.make_order(4)}')
