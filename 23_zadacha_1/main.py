total_summa = 0
line_count = 0
# дополнительная переманная списка ошибок введена,
# что бы не добавлять в файл ошибки по одной и не открывать его постоянн
errors_to_log = []

with open("people.txt", "r") as people_names_file:
    for line in people_names_file:
        line_count += 1
        try:
            if len(line) < 4:
                error_message = 'В ' + str(line_count) + ' строке меньше трех символов, имя: ' + line
                errors_to_log.append(error_message)
                raise ValueError
            else:
                total_summa += len(line)
        except ValueError:
            print(error_message)

print('Сумма всех нормальных имен равна', total_summa)

with open('errors.log', 'w') as errors_file:
    for errors in errors_to_log:
        errors_file.write(errors)
        errors_file.write('\n')