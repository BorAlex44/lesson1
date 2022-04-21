class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.z = complex(a, b)

    def __str__(self):
        return '(%s+%sj)' % (self.a, self.b)

    def __add__(self, other):
        summa = self.z + other.z
        return summa

    def __mul__(self, other):
        mul = self.z * other.z
        return mul


z1 = ComplexNumber(1, 2)
z2 = ComplexNumber(2, 3)
print(f'Первое комплексное число - {z1}')
print(f'Второе комплексное число - {z2}')
print(f'Сумма=', z1 + z2)
print(f'Произведение=', z1*z2)
