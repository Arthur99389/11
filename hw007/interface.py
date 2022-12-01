import delete
import write
import print_all
import edit
import search
import html_export

while True:
    print("База данных сотрудников.\n")
    print('1. Вывести все записи\n2. Добавить запись\n3. Найти запись\n4. Изменить запись\n\
5. Удалить запись\n6. Экспорт справочника в html\n7. Выход\n')

    value = int(input("Выберите действие: "))
    print(value)
    if value == 1:
        print_all.print_all_to_console()
    elif value == 2:
        write.New_Entry('employees.csv')
    elif value == 3:
        search.Search_Entry('employees.csv')
    elif value == 4:
        edit.Edit_Entry('employees.csv')
    elif value == 5:
        delete.delete_str('employees.csv')
    elif value == 6:
        html_export.html_exp()
    elif value == 7:
        break