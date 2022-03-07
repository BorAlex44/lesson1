my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
new_my_list = []
for elem in my_list:
    if elem.isdigit():
        new_my_list.append(f'"{int(elem):02}"')
    elif (elem.startswith('+') or elem.startswith('-')) and elem[1:].isdigit():
        new_my_list.append(f'"{elem[0]}{int(elem):02}"')
    else:
        new_my_list.append(elem)
new_str = ' '.join(new_my_list)
print(new_str)
