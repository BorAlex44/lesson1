price_list = [25.10, 48.58, 32.05, 165.28, 1005.9, 555, 751.12, 65.50, 115.08, 258.45]
for price in price_list:
    rub = int(price)
    kk = (price - int(price))*100
    print(f'{rub} руб {kk:02.0f} коп', end=', ')


print(end='\n')
print(id(price_list))
price_list.sort()
print(id(price_list))
print(price_list)
for price in price_list:
    rub = int(price)
    kk = (price - int(price))*100
    print(f'{rub} руб {kk:02.0f} коп', end=', ')


print(end='\n')
new_price_list = sorted(price_list, reverse=True)
print(new_price_list)
for price in new_price_list[:5]:
    rub = int(price)
    kk = (price - int(price))*100
    print(f'{rub} руб {kk:02.0f} коп', end=', ')


