def fill_schedule(day_name):  # заполнение дня недели временем с 6 утра до 11 вечера
    with open(day_name, 'a', encoding='utf-8') as day_name_name:
        for i in range(6, 24):
            day_name_name.writelines(f'{i}:00\n')
list_key = {0: 'Monday.txt', 1: 'Tuesday.txt', 2: 'Wednesday.txt', 3: 'Thursday',
            4: 'Friday.txt', 5: 'Saturday.txt', 6: 'Sunday.txt'}
choice_user = int(input('Choose,what you want to do with your schedule: \nprint 1 - for read, '
                        'print 2 - for writing, print 3 - for changing, \n0 - for exit: '))
index_day = int(input('Enter day of week: (from 1 to 7): ')) - 1
fill_schedule(list_key[index_day])
while choice_user > 0 and choice_user < 4:
    if index_day=='':
        index_day = int(input('Enter day of week: (from 1 to 7): ')) - 1
    if choice_user == 1:
        with open(list_key[index_day], 'r', encoding='utf-8') as your_day:
            print(your_day.read())
    if choice_user == 2:
        text_training = input('Enter your training: ')
        time_training = int(input("What time to set the alarm: (from 6 to 23 time o'clock) ")) - 6
        with open(list_key[index_day]) as your_day:
            harry_potter = your_day.readlines()  # временная переменная-список для записи исправленной строки
            harry_potter[time_training] = f'{time_training+6}:00 - {text_training}\n'
            with open(list_key[index_day], 'w', encoding='utf-8') as your_day:
                your_day.writelines(harry_potter)
                harry_potter.clear()
    if choice_user == 3:
        text_training = input('Enter your training: ')
        time_training = int(input("What time to set the alarm: (from 6 to 23 time o'clock) ")) - 6
        with open(list_key[index_day]) as your_day:
            harry_potter = your_day.readlines()  # временная переменная-список для записи исправленной строки
            harry_potter[time_training] = f'{harry_potter[time_training]} + {text_training}\n'
            with open(list_key[index_day], 'w', encoding='utf-8') as your_day:
                your_day.writelines(harry_potter)
                harry_potter.clear()
    choice_user = int(input('Choose,what you want to do with your schedule: \nprint 1 - for read, '
                            'print 2 - for writing, print 3 - for changing, \n0 - for exit: '))
    index_day = ''
else:
    print('Досвидосики')

