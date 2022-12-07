# Написать программу, которая генерирует двумерный массив на A x B элементов ( A и B вводим с клавиатуры)
# И считаем средне-арифметическое каждой строки (не пользуемся встроенными методами подсчета суммы)
import random

a = int(input('Enter the numbers of rows: '))
b = int(input(('Enter the numbers of columns: ')))
array1 = []
sum_rows = []
for i in range(b):
    sum_1 = 0
    for j in range(a):
        array1.append(int(random.randint(1, 10)))
        sum_1 += array1[j]
    sum_rows.append(sum_1)
print(array1)
print(sum_rows)
