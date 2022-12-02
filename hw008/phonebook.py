from tkinter import *

def add_contact():
    new_contact = '{name} {surname} {number}'\
                .format(name=entryName.get(),surname=entrySurname.get(),number=entryNumber.get())
    allContacts.insert(END, new_contact)
    entryName.delete(0, END)
    entrySurname.delete(0, END)
    entryNumber.delete(0, END)
    write_contacts()

def delete_contact():
    select = allContacts.curselection()
    allContacts.delete(select[0])
    write_contacts()

def write_contacts():
    data = open('phonebook.txt', 'w', encoding='utf-8')
    for row in allContacts.get(0, END):
        data.writelines(row + '\n')
    data.close()

def view_contacts():
    try:
        data = open('phonebook.txt', 'r', encoding='utf-8')
        for contact in data.readlines():
            allContacts.insert(END, contact.removesuffix('\n'))
        data.close()
    except FileNotFoundError:
        print('Файл не найден')

def edit_contact():
    try:
        select = allContacts.curselection()
        allContacts.delete(select[0])
        add_contact()
    except IndexError:
        print('Запись не выбрана')


root = Tk()
root.geometry('600x400')
root.title('Телефонный справочник')

buttonAddContact = Button(root, text='Добавить контакт', command=add_contact)
buttonAddContact.grid(row=3, column=0, columnspan=2)
buttonDeleteContact = Button(root, text='Удалить контакт', command=delete_contact)
buttonDeleteContact.grid(row=4, column=1)
buttonDeleteContact = Button(root, text='Редактировать контакт', command=edit_contact)
buttonDeleteContact.grid(row=3, column=1)

labelName = Label(root, text='Введите имя')
labelName.grid(row=0, column=0)
labelSurname = Label(root, text='Введите фамилию')
labelSurname.grid(row=1, column=0)
labelNumber = Label(root, text='Введите телефон')
labelNumber.grid(row=2, column=0)

entryName = Entry(root, width=15)
entryName.grid(row=0, column=1)
entrySurname = Entry(root, width=15)
entrySurname.grid(row=1, column=1)
entryNumber = Entry(root, width=15)
entryNumber.grid(row=2, column=1)

allContacts = Listbox(root, height=8, width=45, selectmode=EXTENDED)
allContacts.grid(row=4, column=0)
view_contacts()

root.mainloop()