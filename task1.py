class Matrix:
    def __init__(self, list_of_lines: list):
        self.list_of_lines = list_of_lines
        self.number_line = len(self.list_of_lines)

    def __str__(self):
        return f'{self.list_of_lines[0]}\n{self.list_of_lines[1]}\n{self.list_of_lines[2]}'

    def __add__(self, other):
        new_matrix = [[], [], []]
        for i in range(3):
            for j in range(3):
                new_matrix[i].append(self.list_of_lines[i][j] + other.list_of_lines[i][j])
        return f'{new_matrix[0]}\n{new_matrix[1]}\n{new_matrix[2]}'


first = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
second = Matrix([[10, 11, 12], [13, 14, 15], [16, 17, 18]])
print(f'first matrix:\n{first}\n')
print(f'second matrix: \n{second}\n')
print(f'result matrix: \n{first + second}')
