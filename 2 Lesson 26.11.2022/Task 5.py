# Реализуйте алгоритм перемешивания списка
from random import randint
list = []
len = int(input('Введите длинну списка:'))
for i in range(len):
    list.append(i+1)
print(list)
for i in range(len):
    temp_index = randint(1, len-1)
    temp_val = list[i]
    list[i] = list[temp_index]
    list[temp_index] = temp_val
print(list)