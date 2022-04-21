class MyZeroDivizion(Exception):
    def __init__(self, txt):
        self.txt = txt


class MyFunction:
    @staticmethod
    def division():
        try:
            number_1 = int(input('Введите первое число: '))
            number_2 = int(input('Введите второе число: '))
            if number_2 == 0:
                raise MyZeroDivizion('Ошибка!!!! На ноль делить нельзя!!!!')
            else:
                result = number_1 / number_2
                return result
        except MyZeroDivizion as err:
            return err


print(MyFunction.division())
