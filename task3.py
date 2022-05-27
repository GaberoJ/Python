class Cell:
    def __init__(self, number_of_cells):
        self.number_of_cells = number_of_cells

    def __add__(self, other):
        return self.number_of_cells + other.number_of_cells

    def __sub__(self, other):
        if self.number_of_cells > other.number_of_cells:
            return self.number_of_cells - other.number_of_cells
        else:
            raise ValueError('Невозможно произвести вычитание')

    def __mul__(self, other):
        return self.number_of_cells * other.number_of_cells

    def __floordiv__(self, other):
        return self.number_of_cells // other.number_of_cells

    def make_order(self, num_of_cells_in_row):
        if self.number_of_cells % num_of_cells_in_row == 0:
            result = f'{"*" * num_of_cells_in_row}\\n' * (self.number_of_cells // num_of_cells_in_row)
            return result[:-2]
        else:
            result = f'{"*" * num_of_cells_in_row}\\n' * ((self.number_of_cells // num_of_cells_in_row) + 1)
            return result[:-(num_of_cells_in_row - self.number_of_cells % num_of_cells_in_row + 2)]


first_cell = Cell(12)
second_cell = Cell(7)

print(f'Сложение: {first_cell + second_cell}')
print(f'Вычитание: {first_cell - second_cell}')
print(f'Умножение: {first_cell * second_cell}')
print(f'Целочисленное деление: {first_cell // second_cell}\n')

print(first_cell.make_order(6))
print(first_cell.make_order(5))
print(second_cell.make_order(3))
