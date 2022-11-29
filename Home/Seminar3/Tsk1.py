# 3.10 Вводим с клавиатуры десятичное число. Необходимо перевести его в шестнадцатиричную систему счисления.

num_checking = int(input('enter correct decimal: '))
string_for_number = ''
while num_checking > 0:
    string_for_number_check = num_checking % 16
    if string_for_number_check > 9:
        if string_for_number_check == 10:
            string_for_number_check = 'a'
        if string_for_number_check == 11:
            string_for_number_check = 'b'
        if string_for_number_check == 12:
            string_for_number_check = 'c'
        if string_for_number_check == 13:
            string_for_number_check = 'd'
        if string_for_number_check == 14:
            string_for_number_check = 'e'
        if string_for_number_check == 15:
            string_for_number_check = 'f'
    string_for_number += str(string_for_number_check)
    num_checking = num_checking // 16
print(string_for_number[::-1])
