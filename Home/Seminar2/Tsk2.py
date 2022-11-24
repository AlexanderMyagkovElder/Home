# Вводим с клавиатуры целое число X. Далее вводим Х целых чисел.
# Необходимо вывести на экран максимальное и второе максимальное число из введенных чисел.
x = int(input('Введите количество чисел: '))
number = int(input('Введите число: '))
max_num = number
second_max = 0
for i in range(x - 1):
    number = int(input('Введите число: '))
    if number > second_max:
        if number > max_num:
            second_max = max_num
            max_num = number
        else:
            second_max = number
print(f'Second Maximum = {second_max}, Maximum = {max_num}')
