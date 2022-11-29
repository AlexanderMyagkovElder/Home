# 3.12 Вводим с клаиватуры строку. Необходимо развернуть подстроку между первой и последней буквой "о".
# Если она только одна или её нет - то сообщить, что буква "о" -одна или не встречается
str_user = input('Enter text on English: ')
count = str_user.count('o')
if count == 1:
    print('Letter "O" is only in this text')
elif count == 0:
    print('There is no letter "O"')
else:
    first_o = str_user.find('o')
    str_user_oncontrary = str_user[::-1]
    second_o = str_user_oncontrary.find('o')
    second_o = len(str_user) - second_o - 1
    for i in range(len(str_user)):
        if i>first_o and i<second_o:
            print(str_user_oncontrary[i],end='')
        else:
            print(str_user[i],end='')


