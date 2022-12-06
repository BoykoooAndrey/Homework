# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена
# и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
# - k=4 => 8*(x**4) + 9*(x**3) + 1*(x**2) + 5*x + 4 = 0 или 8*(x**4) + 5*x + 4 = 0 и т.д.
from random import randint
k = int(input("Введите k:"))
list = []
for i in range(k):
    temp = randint(0, 100)
    if i == k-1:
        if temp == 0:
            list.append('= 0')
        else:
            list.append(f'{temp} = 0')
    elif i == k-2:
        if temp == 0:
            continue
        if temp == 1:
            list.append(f'x')
        else:
            list.append(f'{temp}*x')
        list.append('+')
    else:
        if temp == 0:
            continue
        if temp == 1:
            list.append(f'x**{k-i}')
        else:
            list.append(f'{temp}*(x**{k-i})')
        list.append('+')
print(" ".join(list))
