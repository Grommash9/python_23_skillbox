with open("people.txt", "r") as people_names_file:
    for line in people_names_file:
        print(line, end = '')
        if len(line) < 4:
            raise ValueError('В этой строке меньше трех символов')