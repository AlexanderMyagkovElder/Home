# 3.11 Вводим с клавиатуры строку. Необходимо сказать, является ли эта строка дробным числом

string_checking = input('Enter fractional number: ')
print(string_checking.isnumeric)
if string_checking == int(string_checking):
    print('False')
else:
    print('True')
