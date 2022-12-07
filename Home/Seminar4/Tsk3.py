# Сгенерируйте список на 30 элементов. Отсортируйте список по возрастанию, методом
# сортировки выбором
import random

list1 = []
for i in range(31):
    list1.append(random.randint(0, 9))
print(list1)
for i in range(len(list1)):
    min_value = i
    for j in range(i + 1, len(list1)):
        if list1[j] < list1[min_value]:
            min_value = j
    list1[i], list1[min_value] = list1[min_value], list1[i]
print(list1)
