import pprint
import os

def work_with_phonebook():
    choice=show_menu()
    phone_book=read_txt('phon.txt')
    while (choice!=8):
        if choice==1:
            print_result(phone_book)
        elif choice==2:
            last_name=input('Введите фамилию абонента: ')
            print(find_by_lastname(phone_book,last_name))

        elif choice==3:
            number=input('Введите номер телефона абонента: ')
            print(find_by_number(phone_book,number))
	    	
        elif choice==4:
            last_name=input('Введите фамилию абонента: ')
            print(find_by_lastname(phone_book,last_name))
            if type(find_by_lastname(phone_book,last_name)) != type('string'):
                new_number=input('Введите новый номер телефона абонента: ')
                print(change_number(phone_book,last_name,new_number))

        elif choice==5:
            last_name=input('Введите фамилию абонента: ')
            name=input('Введите имя абонента: ')
            number=input('Введите номер телефона абонента: ')
            description=input('Введите описание абонента: ')
            print(add_user(phone_book,last_name,name,number,description))

        elif choice==6:
            last_name=input('Введите фамилию абонента: ')
            if type(find_by_lastname(phone_book,last_name)) != type('string'):
                print(f"Вы точно хотите удалить запись {find_by_lastname(phone_book,last_name)}")
                verdict = input("Введите 'да' или 'нет': ")
                if verdict == "да":
                    phone_book.remove(find_by_lastname(phone_book,last_name))
                    print("Запись успешно удалена!")
            else:
                print("Запись не найдена!")
        elif choice==7:
            write_txt('phon.txt',phone_book)

        choice=show_menu()

def show_menu():
    print('''\nВыберите необходимое действие: 
1. Отобразить весь справочник
2. Найти абонента по фамилии
3. Найти абонента по номеру телефона
4. Изменить номер телефона абонента
5. Добавить абонента в справочник
6. Удалить запись по фамилии
7. Сохранить справочник в текстовом формате
8. Закончить работу\n''')
    choice = int(input("Позиция в меню: "))
    return choice


def read_txt(filename): 
    phone_book=[]
    fields = ['Фамилия', 'Имя', 'Телефон', 'Описание']
    with open(filename,'r',encoding='utf-8-sig') as phb:
        for line in phb:
            line = line.replace('\n', '')
            record = dict(zip(fields, line.split(',')))
			#dict(( (фамилия,Иванов),(имя, Точка),(номер,8928) ))
            phone_book.append(record)
    return phone_book


def write_txt(filename , phone_book):
    with open(filename,'w',encoding='utf-8-sig') as phout:
        for i in range(len(phone_book)):
            s=''
            for v in phone_book[i].values():
                s = s + v + ','
            phout.write(f'{s[:-1]}\n')
    print(f"Запись по адресу {os.path.abspath(filename)} прошла успешно!")

def print_result(phone_book):
    print("\nТелефонный справочник:\n")
    for z in phone_book:
        pprint.pprint(z, sort_dicts=False)
        print("")

def find_by_lastname(phone_book,last_name):
        for z in phone_book:
            if z['Фамилия'] == last_name:
                return z
        return "Запись не найдена!"
        # return (list(filter(lambda x: x["Фамилия"] == last_name, phone_book)))

def find_by_number(phone_book,number):
        for z in phone_book:
            if z['Телефон'] == number:
                return z
        return "Запись не найдена!"

def change_number(phone_book,last_name,new_number):
    find_by_lastname(phone_book,last_name)['Телефон'] = new_number
    return f"Телефон для абонента {last_name} успешно изменен на: {new_number}"
    
def add_user(phone_book,last_name,name,number,description):
    card = {'Фамилия': last_name,
                    'Имя': name,
                    'Телефон': number,
                    'Описание': description}
    phone_book.append(card)
    return f'Запись {card} успешно добавлена'

work_with_phonebook()



