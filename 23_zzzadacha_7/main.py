def new_line_remover(line):
    if line.endswith('\n'):
        return line[:-1]
    else:
        return line


def validator(line):
    temp_data_list = line.split(' ')
    try:
        if not len(temp_data_list) == 3:
            raise TypeError
        if int(temp_data_list[0]) != int(temp_data_list[0]) or int(temp_data_list[2]) != int(temp_data_list[2]):
            raise ValueError
        if not temp_data_list[1] in all_operators:
            raise SyntaxError
        else:
            for symbols in zero_problems:
                if temp_data_list[1] == symbols:
                    if int(temp_data_list[2]) == 0:
                        raise ZeroDivisionError
    except TypeError:
        print('(', line, ')' + ' Ошибка ввода: ожидаеться три аргумента,'
                               ' а было введено', len(temp_data_list), end='.')
        return
    except ValueError:
        print('(', line, ')' + ' Неверные значения переменных', end='.')
        return
    except SyntaxError:
        print('(', line, ')' + ' Неверное значение оператора', end='.')
        return
    except ZeroDivisionError:
        print('(', line, ')' + ' Попытка деления на ноль', end='.')
        return
    else:
        return operation_dict[temp_data_list[1]](int(temp_data_list[0]), int(temp_data_list[2]))


operation_dict = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '/': lambda x, y: x / y,
    '//': lambda x, y: x // y,
    '*': lambda x, y: x * y,
    '**': lambda x, y: x ** y,
    '%': lambda x, y: x % y
}

total_summa = 0
all_operators = ['+', '-', '/', '//', '*', '**', '%']
zero_problems = ['/', '//', '%']

with open('calc.txt', 'r') as data_file:
    for line in data_file:
        formatted_line = new_line_remover(line)
        result = validator(formatted_line)
        while result == None:
            desire_to_fix = input(' Хотите исправить? (да/нет): ')
            if desire_to_fix == 'да':
                new_line = input('Введите исправленную строку: ')
                formatted_line = new_line_remover(new_line)
                result = validator(formatted_line)
            else:
                result = 0
                break
        if result != 0:
            total_summa += result
            print('(', formatted_line, ') = ', result)

print('\nСумма результатов всех правильных выражений:', total_summa)
