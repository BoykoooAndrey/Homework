# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий
# сумму многочленов (складываются числа, у которых "х" в одинаковых степенях). Пример того, что будет в
# итогвом файле: 8*(x**4) + 9*(x**3) + 1*(x**2) + 5*x + 4 = 0
def find_degree(list1, list2, x):
    temp_val_list = []
    for i in range(len(list1)):
        if x == 1 and ("*x" in list1[i]):
            if "=" in list1[i]:
                temp_val_list.append((list1[i])[:3])
            else:
                temp_val_list.append(list1[i])
            break
        elif (f"(x**{x})" in list1[i]):
            temp_val_list.append(list1[i])

        if x == 0 and ('=' in list1[i] and not 'x =' in list1[i]):
            temp_val_list.append(list1[len(list1)-1])

    for i in range(len(list2)):
        if x == 1 and ("*x" in list2[i]):
            if "=" in list2[i]:
                temp_val_list.append((list2[i])[:3])
            else:
                temp_val_list.append(list2[i])
            break
        elif (f"(x**{x})" in list2[i]):
            temp_val_list.append(list2[i])

        if x == 0 and ('=' in list2[i] and not 'x =' in list2[i]):
            temp_val_list.append(list2[len(list2)-1])

    return temp_val_list


file_ptath1 = 'example1.txt'
file_ptath2 = 'example2.txt'
example1 = None
example2 = None

with open(file_ptath1, 'r') as list11:
    example1 = list11.read().split(' + ')
with open(file_ptath2, 'r') as list22:
    example2 = list22.read().split(' + ')

max_size = max(len(example1), len(example2))
res_list = []

for i in range(max_size - 1, -1, -1):
    list = find_degree(example1, example2, i)
    if (len(list) == 2):
        temp_val = str(int((list[0])[0])+int((list[1])[0]))
        string1 = list[0].replace((list[0])[0], temp_val)
        res_list.append(string1)
    else:
        res_list.append(list[0])


print(' + '.join(res_list))
