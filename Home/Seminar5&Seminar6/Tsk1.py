# 1) Сделать игру морской бой
import random

def random_ship(list, row, column):
    random_row = random.randrange(row)
    random_column = random.randrange(column)
    list[random_row][random_column] = 1

field_of_battle = []
for i in range(2):
    list_row = []
    for j in range(2):
        list_row.append(0)
    field_of_battle.append(list_row)
random_ship(field_of_battle, 2, 2)
# Почему не работает этот кусок? чтобы вводить координаты, пока не попадешь?
# while True:
#     try:
#         target_row = int(input('Enter location target: row = ')) - 1
#         target_column = int(input('Enter location target: column = ')) - 1
#         if field_of_battle[target_row][target_column] != 1:
#             print('You miss')
#         else:
#             print('Kill')
#     except ValueError:
#         print('enter numbers!!!')
target_row = int(input('Enter location target: row = ')) - 1
target_column = int(input('Enter location target: column = ')) - 1
if field_of_battle[target_row][target_column] != 1:
    print('You miss')
else:
    print('Kill')
for i in field_of_battle:
    print(i)
