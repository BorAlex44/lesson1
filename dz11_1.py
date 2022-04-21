class Data:
    def __init__(self, data_str: str):
        self.data_str = data_str

    @classmethod
    def data_int(cls, data_str):
        try:
            return list(map(int, data_str.split('-')))
        except Exception:
            raise f"Не получилось разбить стоку на цифры"

    @staticmethod
    def valid_data(data_str):
        day: int
        month: int
        year: int
        try:
            day, month, year = Data.data_int(data_str)
        except Exception:
            raise f'Что то пошло не так'

        if not 1 <= month <= 12:
            return f'Такого месяца не существует'
        if not 0 <= year:
            return f'Проверьте правильность ввода года'
        if not 1 <= day <= 31:
            return f'Неправильнно введен день'
        if month == 2 and day == 29 and year % 4 != 0 and year % 100 != 0 and year % 400 != 0:
            return f'В этом феврале не может быть 29 дней'
        return f'Дата корректна'


print(Data.data_int('12-11-2021'))
print(Data.valid_data('12-11-2021'))
today = Data('12-11-2021')
print(today.data_int('10-12-2000'))
print(Data.valid_data('29-2-2021'))
print(Data.valid_data('35-11-2021'))
