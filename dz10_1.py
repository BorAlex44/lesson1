class Matrix:
    def __init__(self, my_matrix):
        self.my_matrix = my_matrix

    def __str__(self):
        return '\n'.join(map(str, self.my_matrix))

    def __add__(self, other):
        new_matrix = []
        if len(self.my_matrix) == len(other.my_matrix):
            for line_1, line_2 in zip(self.my_matrix, other.my_matrix):
                if len(line_1) != len(line_2):
                    return 'Problem with the length of the matrix'

                sum_line = [x + y for x, y in zip(line_1, line_2)]
                new_matrix.append(sum_line)
        else:
            return 'Problem with the length of the matrix'
        return Matrix(new_matrix)


matrix_1 = Matrix([[3, 5, 2], [7, 2, 1], [1, 4, 3]])
matrix_2 = Matrix([[1, 3, 2], [2, 6, 8], [3, 5, 5]])
print(matrix_1)
print('_'*60)
print(matrix_2)
print('_'*60)
print(matrix_1 + matrix_2)
