
def number_func():
    return int(input('1- добавить контакт \n2 - поиск \n3 - показать телефонную книгу \n4 - удалить контакт\n->'))

def search():
    return str(input('Поиск:'))

def request():
    list = []
    list.append(input('Введите имя:'))
    list.append(input('Введите фамилию:'))
    list.append(input('Введите номер телефона:'))
    list.append(input('Введите примечание:'))
    return list

def del_cont_name():
    return int(input('Введите индекс контакта который хотите удалить:'))