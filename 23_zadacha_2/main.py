import random

results = []


def divider(a, b):
    try:
        a / b
    except ZeroDivisionError:
        print(a, '/', b)
        print('Была попытка деления на ноль, вместо резульатата будет внесен прочерк')
        return '-'
    return a / b


def calculations(x, y, action='+'):
    if action == '-':
        x -= random.randint(0, 5)
        y -= random.randint(0, 10)
        return divider(x, y)
    else:
        x += random.randint(0, 5)
        y += random.randint(0, 10)
        return divider(y, x)


with open('coordinates.txt', 'r') as data_from_file:
    for line in data_from_file:
        income_data = line.split(' ')
        temp_list = [random.randint(0, 100), calculations(int(income_data[0]), int(income_data[1])),
                     calculations(int(income_data[0]), int(income_data[1]), '-')]
        results.append(set(temp_list))

with open('result.txt', 'w') as results_file:
    for data in results:
        for numbers in data:
            results_file.write(str(numbers))
            results_file.write(' ')
        results_file.write('\n')
