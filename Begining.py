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

# s='ronaldo'
# x='fhjg'
# print(' '.join([s,x]))
# s='''now everybody, who love 3-1-3
# put your motherfucker hands and follow
# me'''
# print(s)
#

# x=random.triangular(1,5)
# print(x)
# string = 'ronaldo'
# print(string.find('o',3,))
# random_index = random.randint(0, len(string) - 1)
# char = string[random_index]
# print(char)

# f = open('D:/study/Python/pythonProject/Home/test.txt', 'r')
# f.close()
# with open ('test.txt','r') as f:
#     print(f.read(5))


# 3.5 Вводим любую строку и нужно посчитать кол-во символов в верхнем регистре


# 3.6 Безопасный пароль. Пользователь вбивает пароль.
# Нужно сказать - безопасный он или нет. Безопасным считается, если он от 8 символов, есть верхний и нижний регистр. А так же цифры. Можеет, при желании, добавить и спец. символы

# 3.7 Вводим строку с клавиатуры. Необходимо сказать, какой символ встречается чаще всего


# 3.8 Написать программу, которая скажет в веденной строке индекс второго символа "в"
#
# day=int(input("enter for 1 to 3: "))
# list_of_week = {1: 'first.txt', 2: 'second.txt', 3: 'third.txt'}
# with open(list_of_week[day],'a',encoding='utf-8') as what_s :
#     what_s.writelines('1')
# with open(list_of_week[day],'a',encoding='utf-8') as what_s :
#     what_s.writelines('2')
#     print(what_s.readline)
#
# class Time:
#     def __init__(self,minutes,seconds):
#         self.mi
# import request
# response= request.get('http://mail.ru')
# print(response)
import re
# x=5
# s='x *8'
# s1=eval(s)
# print(s1.__sizeof__())
# z=[2,3,4,5,6,7]
# xc=['cris','crisht','cr7','cristiano']
# xc.sort(key=lambda y:y[-2])
# xd={'kir','ol','sir','ol','as'}
# print(xd)

from datetime import datetime as dt

# time_now=dt.now().strftime('%H:%M')
# print(time_now)

class Soup():
    def Is_it(self,component):
        if component=='свекла':
            print('borszcz')
        elif component=='капуста':
            print('szczii')
        elif component=='горох':
            print('peasing soup')
        else:
            print(f'just water with {component}')
a=Soup()
a.Is_it('боб')
