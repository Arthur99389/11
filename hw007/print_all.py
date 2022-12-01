def print_all_to_console():
    with open('employees.csv', 'r') as data:
        print('ID    Фамилия    Имя    Отчество    Телефон    Отдел    Должность')
        for line in data:
            print(line.replace(',', ' ').removesuffix('\n'))