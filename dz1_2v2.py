numbers = []
for number in range(1, 1001, 2):
    numbers.append(number**3)

summa_seven = 0
new_array_numbers = []
for number in numbers:
    summa = 0
    temp_number = number
    while temp_number != 0:
        summa = summa + temp_number % 10
        temp_number = temp_number // 10
    if summa % 7 == 0:
        summa_seven = summa_seven + number
print(summa_seven)

new_summa_seven = 0
for number in numbers:
    new_summa = 0
    new_temp_number = number + 17
    while new_temp_number != 0:
        new_summa = new_summa + new_temp_number % 10
        new_temp_number = new_temp_number // 10
    if new_summa % 7 == 0:
        new_summa_seven = new_summa_seven + number + 17
print(new_summa_seven)
