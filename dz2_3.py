my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
i = 0
while i < len(my_list):
    if my_list[i].isdigit():
        my_list.insert(i, '"')
        my_list[i+1] = f'{int(my_list[i+1]):02}'
        my_list.insert(i+2, '"')
        i += 2
    elif (my_list[i].startswith('+') or my_list[i].startswith('-')) and my_list[i][1:].isdigit():
        my_list.insert(i, '"')
        my_list[i+1] = f'{my_list[i+1][0]}{int(my_list[i+1]):02}'
        my_list.insert(i+2, '"')
        i += 2
    i += 1
new_str = ' '.join(my_list)
print(new_str)
