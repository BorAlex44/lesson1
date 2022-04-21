class NotNumber(Exception):
    def __init__(self, txt):
        self.txt = txt


def data_check():
    my_list = []
    while True:
        try:
            data = input('Введите данные: ')
            if data == 'stop':
                break
            elif not data.isdigit():
                raise NotNumber(data)
            else:
                my_list.append(data)
        except NotNumber:
            print('ОШИБКА!!!!!! Введенные данные не являются числом!!!!!!')
    return my_list


print(data_check())
