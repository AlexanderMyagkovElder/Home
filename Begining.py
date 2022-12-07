# num1=int(input("Введите 1 число: "))
# num2=int(input("Введите 2 число: "))
# if num2==num1**2:
#     print("Да. является")
# elif num1==num2**2:
#     print("Да. является")
# else:
#     print("Нет, не является")
# Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.
# 1, 4, 8, 7, 5 -> 8

# num1 = int(input("Введите число: "))
# num2 = int(input("Введите число: "))
# num3 = int(input("Введите число: "))
# num4 = int(input("Введите число: "))
# num5 = int(input("Введите число: "))
# list = []
# list.append(num1)
# list.append(num2)
# list.append(num3)
# list.append(num4)
# list.append(num5)
# max_number = list[0]
# for i in range(0, 5):
#     if list[i] > max_number:
#         max_number = list[i]
# # if num2>max_number:
# #     max_number=num2
# print(max_number)

# name,surname = 'sanches', 'panches'
# print('My name is '+name, 'My surname is '+surname,sep='jhgg',end='ny ')
# print("I'm a {1},{0}".format(name,surname),sep='aaa')
# print(name*2,file=someone.txt)

# s = 'fddfsg'
# print(s.replace('(0: len(s) / 2), (len(s) / 2: len(s))'))
# import random
#
# min = random.randint()
# print(min)

# name = 'hvk'
# age = '12'
# filter_age = filter_string(name, 'h')
# print(f'my name {name}, my age {filter_age}')
# string_1='bhjjk'
# print(set(string_1))
import math
import random


def count_banknotes(count25, salary):
    count10, count3, count1 = 0, 0, 0

    salary -= count25 * 25
    count10 = salary // 10
    salary -= count10 * 10
    count3 = salary // 3
    count1 = salary - count3 * 3


    total_count = count1 + count3 + count10 + count25
    summary = (f'Минимальное количество купюр, которыми можно выдать зарплату - {total_count}.\n'
               f'25 рублевыми купюрами - {count25} шт.\n'
               f'10 рублевыми купюрами - {count10} шт.\n'
               f'3 рублевыми купюрами - {count3} шт.\n'
               f'1 рублевыми купюрами - {count1} шт.')

    return total_count, summary

# s='ronaldo'
# x='fhjg'
# print(' '.join([s,x]))
# s='''now everybody, who love 3-1-3
# put your motherfucker hands and follow
# me'''
# print(s)


# x=random.triangular(1,5)
# print(x)
# string = 'ronaldo'
# print(string.find('o',3,))
# random_index = random.randint(0, len(string) - 1)
# char = string[random_index]
# print(char)

# 3.5 Вводим любую строку и нужно посчитать кол-во символов в верхнем регистре


# 3.6 Безопасный пароль. Пользователь вбивает пароль.
# Нужно сказать - безопасный он или нет. Безопасным считается, если он от 8 символов, есть верхний и нижний регистр. А так же цифры. Можеет, при желании, добавить и спец. символы

# 3.7 Вводим строку с клавиатуры. Необходимо сказать, какой символ встречается чаще всего


# 3.8 Написать программу, которая скажет в веденной строке индекс второго символа "в"
