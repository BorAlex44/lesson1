numbers = []
for number in range(1, 1001, 2):
    numbers.append(number**3)
#print(numbers)

new_array_number = []
for number in numbers:
    summa = 0
    for i in str(number):
        summa += int(i)
    if summa % 7 == 0:
        new_array_number.append(number)
#print(new_array_number)

summa = 0
for number in new_array_number:
    summa = summa + number
print(summa)

number_plus_seven = []
for number in numbers:
    new_number = number + 17
    number_plus_seven.append(new_number)
#print(number_plus_seven)

new_number_plus_seven = []
for number in number_plus_seven:
    summa = 0
    for i in str(number):
        summa += int(i)
    if summa % 7 == 0:
        new_number_plus_seven.append(number)

new_summa = 0
for number in new_number_plus_seven:
    new_summa = new_summa + number
print(new_summa)
