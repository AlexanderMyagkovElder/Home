# 3.11 Вводим с клавиатуры строку. Необходимо сказать, является ли эта строка дробным числом

string_checking = float(input('Enter fractional number: '))
if string_checking == int(string_checking):
    print('False')
else:
    print('True')
