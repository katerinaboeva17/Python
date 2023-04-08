def show_data():
    with open('book.txt', 'r', encoding='utf-8') as f:
        print(f.read())


def add_data():
    fio = input('Введите ФИО: ')
    tel_number = input('Введите номер телефона: ')
    with open('book.txt', 'a', encoding='utf-8') as f:
        f.write(f'\n{fio} | {tel_number}')
    print('Успешно!')

def find_data():
    data = input('Введите данные для поиска: ')
    with open('book.txt', 'r', encoding='utf-8') as f:
        tel_book = f.read()
    print('Результаты поиска: ')
    print(search(tel_book, data))

def search(book: str, info: str):
    book = book.split('\n')
    return '\n'.join([post for post in book if info in post])

def edit_data():
    with open('book.txt', 'r', encoding='utf-8') as f:
        tel_book = f.read()
    tel_book = tel_book.split('\n')
    num = int(input('Введите номер записи, которую хотите изменить: '))
    tel_book[num] = edited(tel_book[num])
    tel_book = '\n'.join(tel_book)
    with open('book.txt', 'w', encoding='utf-8') as f:
        f.write(tel_book)
    print(tel_book)

def edited(text: str):
    fio = input('Введите ФИО: ')
    number = input('Введите номер телефона: ')
    if len(fio) == 0:
        fio = text.split(' | ')[0]
    if len(number) == 0:
        number = text.split(' | ')[1]
    return f'{fio} | {number}'

def del_data():
    with open('book.txt', 'r', encoding='utf-8') as f:
        tel_book = f.read()
    tel_book = tel_book.split('\n')
    num = int(input('Введите номер записи, которую хотите удалить: '))
    tel_book.pop(num)
    tel_book = '\n'.join(tel_book)
    with open('book.txt', 'w', encoding='utf-8') as f:
        f.write(tel_book)
    





    


    
