# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и
# минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 10.01] => 0.19
list = [1.1, 1.2, 0.1, 10.01]
remains = []
for i in range(len(list)):
    remains.append(list[i] - (int(list[i]))) 
min = remains[i]
max = remains[i]
for i in range(len(remains)):
    if remains[i] < min:
        min = remains[i]
    if remains[i] > max:
        max = remains[i]
print(f'{list} => {round(max - min, 2)}')
