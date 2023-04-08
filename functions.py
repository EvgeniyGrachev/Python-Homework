def show_data() -> None: # Выводит информацию справочника
    with open('book.txt', 'r', encoding='utf-8') as f:
        print(f.read())

def add_data() -> None: # Добавляет информацию в справочник
    fio = input("Введите ФИО: ")
    tel_namber = input("Введите номер телефона: ")
    with open('book.txt', 'a', encoding='utf-8') as f:
        f.write(f'\n{fio} | {tel_namber}')
    print("Успешно!")

def find_data() -> None: # Осуществляет поиск по справочнику
    data = input("Введите данные для поиска: ")
    with open('book.txt', 'r', encoding='utf-8') as f:
        tel_book = f.read()
    print(f"Результат поиска:\n{search(tel_book, data)}")

def search(book: str, info: str) -> str: # Находит нужную запись в строке
    book = book.split('\n')
    return '\n'.join([post for post in book if info in post])

def edited(text: str) -> str: # Определяет, что удалить: ФИО или телефон
    fio = input("Введите новое ФИО: ")
    tel_number = input("Введите новый номер телефона: ")
    if len(fio) == 0:
        fio = text.split(' | ')[0]
    if len(tel_number) == 0:
        tel_number = text.split(' | ')[1] 
    return f'{fio} | {tel_number}'

def replace_data() -> None: # Перезаписывает данные
    with open('book.txt', 'r', encoding='utf-8') as f:
        read_list = f.read()
    res_list = read_list.split('\n')
    data = input("Введите данные для поиска: ")
    search_list = search(read_list, data)
    print(f"Результат поиска:\n{search_list}")
    res_list[res_list.index(search_list)] = edited(search_list)
    with open('book.txt', 'w', encoding='utf-8') as f:
        f.write('\n'.join(res_list))   
    print("Успешно!")

def del_data() -> None: # Удаляет данные
    with open('book.txt', 'r', encoding='utf-8') as f:
        read_list = f.read()
    res_list = read_list.split('\n')
    data = input("Введите данные для удаления: ")
    search_list = search(read_list, data)
    print(f"Результат поиска:\n{search_list}")
    ask = int(input("Удалить?\nYES - 1; NO - 2: "))
    if ask == 1:
        res_list[res_list.index(search_list)] = search_list.replace(search_list,"")
        with open('book.txt', 'w', encoding='utf-8') as f:
            f.write('\n'.join(res_list))   
        print("Успешно!")