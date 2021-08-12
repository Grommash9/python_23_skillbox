import random
summa = 0
try:
    with open('try_list.txt', 'w') as list_of_attempts:
        while summa < 777:
            number = int(input('Введите число: '))
            summa += number
            chance_to_close = random.randint(0, 13)
            if chance_to_close != 5:
                list_of_attempts.write(str(number))
                list_of_attempts.write('\n')
            else:
                raise BaseException
except BaseException:
    print('Вызвана случайная ошибка, завершение программы')
    exit()
else:
    print('Введенная вами сумма чисел достигла 777 или превысила это значение, программа завершена')
