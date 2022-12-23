import csv
import input
import pandas as pd

# Функция записи контакта
def rec():
    with open("tel_dir.csv", 'a', newline='') as f:
        csv.writer(f).writerow(input.request())


# Функция поиска контакта
def find_cont(x):
    with open("tel_dir.csv", 'r') as f:
        for i in csv.reader(f):
            for j in i:
                if x in j:
                    print(i)
                    break


# Просмотр телефонной книги
def view_conts():
    tel_dir = pd.read_csv('tel_dir.csv')
    print(tel_dir)



#Удаление контакта
def del_cont(x):
    tel_dir = pd.read_csv('tel_dir.csv')
    tel_dir.drop(labels = [x],axis = 0, inplace = True)
    tel_dir.to_csv('tel_dir.csv', index=False)
