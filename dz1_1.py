duration = int(input('Введите время в секундах: '))
if 0 < duration < 60:
    print(duration, 'сек.')
elif 60 <= duration < 3600:
    minutes = duration // 60
    duration = duration % 60
    print(minutes, 'мин. ', duration, 'сек.')
elif 3600 <= duration < 86400:
    hour = duration // 3600
    duration = duration % 3600
    minutes = duration // 60
    duration = duration % 60
    print(hour, 'час. ', minutes, 'мин. ', duration, 'сек.')
else:
    day = duration // 86400
    duration = duration % 86400
    hour = duration // 3600
    minutes = duration // 60
    duration = duration % 60
    print(day, 'дн. ', hour, 'час. ', minutes, 'мин. ', duration, 'сек.')
