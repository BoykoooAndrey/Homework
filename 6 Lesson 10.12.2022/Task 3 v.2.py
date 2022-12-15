# Реализуйте алгоритм перемешивания списка
from random import randint

len = int(input('Введите длинну списка:'))
list = [i+1 for i in range(len)]
print(list)
for i in range(len):
    temp_index = randint(1, len-1)
    temp_val = list[i]
    list[i] = list[temp_index]
    list[temp_index] = temp_val
print(list)