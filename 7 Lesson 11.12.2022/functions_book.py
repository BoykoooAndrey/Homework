import csv
import pandas as pd


# Функция поиска контакта
def find_cont(x):
    with open("tel_dir.csv", 'r') as f:
        find_list = []
        find_list. append(['Name','Surname','Number','Note'])
        for i in csv.reader(f):
            for j in i:
                if x in j:
                    find_list. append(i)
                    break
        return find_list
# Просмотр телефонной книги
def view_conts():
    with open("tel_dir.csv", 'r') as f:
        tel_dir = csv.reader(f)
        list = []
        for i in tel_dir:
            list.append(i)
        return list

#Удаление контакта
def del_cont(x):
    tel_dir = pd.read_csv('tel_dir.csv')
    tel_dir.drop(labels = [x],axis = 0, inplace = True)
    tel_dir.to_csv('tel_dir.csv', index=False)

