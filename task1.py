class Matrix:
    def __init__(self, list_of_lines):
        self.list_of_lines = list_of_lines

    def __add__(self, other):
        new_matrix = []
        if len(self.list_of_lines) != len(other.list_of_lines):
            print('Неверная матрица: разная размерность')
            exit(0)
        for i in range(len(self.list_of_lines)):
            new_matrix.append([])
            for j in range(len(self.list_of_lines)):
                new_matrix[i].append(self.list_of_lines[i][j] + other.list_of_lines[i][j])
        return Matrix(new_matrix)

    def __str__(self):
        result = ''
        for i in range(len(self.list_of_lines)):
            result += f'{self.list_of_lines[i]}\n'.replace('[', '|').replace(']', '|').replace(',', '')
        return result


ex = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
ex1 = Matrix([[7, 1, 5], [2, 5, 8], [1, 11, 10]])
ex2 = Matrix([[1, 2], [4, 5]])
ex3 = Matrix([[3, 2], [1, 8]])

a = ex + ex1
print(a)
print(a + ex)
print(ex2 + ex3)
error = ex + ex3
