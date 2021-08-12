def file_cleaner(file_name):
    file = open(file_name, 'w')
    file.write('')


def result_saver(file, result):
    file_to_write = open(file, 'a')
    file_to_write.write(result)
    file_to_write.write('\n')
    file_to_write.close()


def is_good_checker(registration_data):
    try:
        if registration_data.endswith('\n'):
            formatted_registration_data = registration_data[:-1]
        else:
            formatted_registration_data = registration_data
        data_list = formatted_registration_data.split(' ')
        if len(data_list) < 3:
            raise ValueError
        for letters in data_list[0]:
            if not letters.isalpha():
                raise NameError
        if not '@' in data_list[1] or not '.' in data_list[1]:
            raise SyntaxError
        if not 0 < int(data_list[2]) < 99:
            raise ValueError
    except ValueError:
        result_saver('registrations_bad.log', formatted_registration_data + ' // error type: ValueError')
    except NameError:
        result_saver('registrations_bad.log', formatted_registration_data + ' // error type: NameError')
    except SyntaxError:
        result_saver('registrations_bad.log', formatted_registration_data + ' // error type: SyntaxError')
    else:
        result_saver('registrations_good.log', formatted_registration_data)


file_cleaner('registrations_good.log')
file_cleaner('registrations_bad.log')

with open('registrations.txt', 'r') as registration_data:
    for line in registration_data:
        is_good_checker(line)
