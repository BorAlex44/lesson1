class Cell:
    def __init__(self, nums):
        self.nums = nums

    def __str__(self):
        return str(self.nums)

    def __add__(self, other):
        return Cell(self.nums + other.nums)

    def __sub__(self, other):
        if self.nums - other.nums > 0:
            return Cell(self.nums - other.nums)
        else:
            'Ячеек в первой клетке меньше или равно второй!!!! Вычитание не возможно!!!!'

    def __mul__(self, other):
        return Cell(self.nums * other.nums)

    def __truediv__(self, other):
        return Cell(round(self.nums / other.nums))

    def make_order(self, rows):
        return '\n'.join(['*' * rows for _ in range(self.nums // rows)]) + '\n' + '*' * (self.nums % rows)


cell_1 = Cell(45)
cell_2 = Cell(9)
print(cell_1)
print(cell_2)
print(cell_1 - cell_2)
print(cell_1 + cell_2)
print(cell_1 / cell_2)
print(cell_1 * cell_2)
print(cell_1.make_order(10))
