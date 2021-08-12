# старый добрый калькулятор через кучу ифов


def calculation(operator, x, y):
    if operator == '+':
        return x + y
    elif operator == '-':
        return x - y
    elif operator == '/':
        return x / y
    elif operator == '//':
        return x // y
    elif operator == '*':
        return x * y
    elif operator == '**':
        return x ** y
    elif operator == '%':
        return x % y


total_summa = 0
all_operators = ['+', '-', '/', '//', '*', '**', '%']
zero_problems = ['/', '//', '%']

with open('calc.txt', 'r') as data_file:
    for line in data_file:
        if line.endswith('\n'):
            formatted_line = line[:-1]
        else:
            formatted_line = line
        temp_data_list = formatted_line.split(' ')
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
            print('(', formatted_line, ')' + ' Ошибка ввода: ожидаеться три аргумента,'
                                             ' а было введено', len(temp_data_list))
        except ValueError:
            print('(', formatted_line, ')' + ' Неверные значения переменных')
        except SyntaxError:
            print('(', formatted_line, ')' + ' Неверное значение оператора')
        except ZeroDivisionError:
            print('(', formatted_line, ')' + ' Попытка деления на ноль')
        else:
            result = calculation(temp_data_list[1], int(temp_data_list[0]), int(temp_data_list[2]))
            total_summa += result
            print('(', formatted_line, ') = ', result)

print('\nСумма результатов всех правильных выражений:', total_summa)


# Реализация через лямбду, мы ещё не учили такое, но я не хочу делать через кучу ифов

# operation_dict = {
#     '+': lambda x, y: x + y,
#     '-': lambda x, y: x - y,
#     '/': lambda x, y: x / y,
#     '//': lambda x, y: x // y,
#     '*': lambda x, y: x * y,
#     '**': lambda x, y: x ** y,
#     '%': lambda x, y: x % y
#     }
#
#
# total_summa = 0
# all_operators = ['+', '-', '/', '//', '*', '**', '%']
# zero_problems = ['/', '//', '%']
#
# with open('calc.txt', 'r') as data_file:
#     for line in data_file:
#         if line.endswith('\n'):
#             formatted_line = line[:-1]
#         else:
#             formatted_line = line
#         temp_data_list = formatted_line.split(' ')
#         try:
#             if not len(temp_data_list) == 3:
#                 raise TypeError
#             if int(temp_data_list[0]) != int(temp_data_list[0]) or int(temp_data_list[2]) != int(temp_data_list[2]):
#                 raise ValueError
#             if not temp_data_list[1] in all_operators:
#                 raise SyntaxError
#             else:
#                 for symbols in zero_problems:
#                     if temp_data_list[1] == symbols:
#                         if int(temp_data_list[2]) == 0:
#                             raise ZeroDivisionError
#         except TypeError:
#             print('(', formatted_line, ')' + ' Ошибка ввода: ожидаеться три аргумента,'
#                                              ' а было введено', len(temp_data_list))
#         except ValueError:
#             print('(', formatted_line, ')' + ' Неверные значения переменных')
#         except SyntaxError:
#             print('(', formatted_line, ')' + ' Неверное значение оператора')
#         except ZeroDivisionError:
#             print('(', formatted_line, ')' + ' Попытка деления на ноль')
#         else:
#             result = operation_dict[temp_data_list[1]](int(temp_data_list[0]), int(temp_data_list[2]))
#             total_summa += result
#             print('(', formatted_line, ') = ', result)
#
# print('\nСумма результатов всех правильных выражений:', total_summa)


# Вариант не через лямбду, а через оператор, мы такое не учили, но я не хочу через кучу ифов делать
# import operator
#
#
# def calculation(symbol, x, y):
#     operation_dict = {
#         '+': operator.add(x, y),
#         '-': operator.sub(x, y),
#         '/': operator.truediv(x, y),
#         '//': operator.floordiv(x, y),
#         '*': operator.mul(x, y),
#         '**': operator.pow(x, y),
#         '%': operator.mod(x, y)
#         }
#     return operation_dict[symbol]
#
#
# total_summa = 0
# all_operators = ['+', '-', '/', '//', '*', '**', '%']
# zero_problems = ['/', '//', '%']
#
# with open('calc.txt', 'r') as data_file:
#     for line in data_file:
#         if line.endswith('\n'):
#             formatted_line = line[:-1]
#         else:
#             formatted_line = line
#         temp_data_list = formatted_line.split(' ')
#         try:
#             if not len(temp_data_list) == 3:
#                 raise TypeError
#             if int(temp_data_list[0]) != int(temp_data_list[0]) or int(temp_data_list[2]) != int(temp_data_list[2]):
#                 raise ValueError
#             if not temp_data_list[1] in all_operators:
#                 raise SyntaxError
#             else:
#                 for symbols in zero_problems:
#                     if temp_data_list[1] == symbols:
#                         if int(temp_data_list[2]) == 0:
#                             raise ZeroDivisionError
#         except TypeError:
#             print('(', formatted_line, ')' + ' Ошибка ввода: ожидаеться три аргумента,'
#                                              ' а было введено', len(temp_data_list))
#         except ValueError:
#             print('(', formatted_line, ')' + ' Неверные значения переменных')
#         except SyntaxError:
#             print('(', formatted_line, ')' + ' Неверное значение оператора')
#         except ZeroDivisionError:
#             print('(', formatted_line, ')' + ' Попытка деления на ноль')
#         else:
#             result = calculation(temp_data_list[1], int(temp_data_list[0]), int(temp_data_list[2]))
#             total_summa += result
#             print('(', formatted_line, ') = ', result)
#
# print('\nСумма результатов всех правильных выражений:', total_summa)
