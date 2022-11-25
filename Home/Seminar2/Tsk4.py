# Вводим с клавиатуры многозначное число.Необходимо узнать и сказать последовательность цифр
# этого числа при просмотре слева направо упорядочена по возрастанию или нет.
# Например 1579 - да ( 1 меньше 5, 5 меньше 7, а 7 меньше 9), 1427 - нет

number = int(input('Введите многозначное число: '))
max_number = number % 10
number = number // 10
while number > 1:
    second_max = number % 10
    number = number // 10
    if second_max > max_number:
        print('последовательность не упорядочена')
        number = 0
    max_number = second_max
if number < 10 and number > 0:
    print('последовательность упорядочена')
