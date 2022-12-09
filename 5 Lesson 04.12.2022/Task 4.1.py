# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

#Cжтие

input = 'input.txt'
output = 'output.txt'

with open(input, 'r') as f:
    temp = f.read()
    list = []
    for i in range(0, len(temp)):
        count = 0
        if not (temp[i] in list):
            for j in range(0, len(temp)):
                if temp[i] == temp[j]:
                    count += 1
        else:
            continue
        list.append(str(count))
        list.append(temp[i])
    with open(output, 'a') as f:
        f.writelines(' '.join(list))

print(' '.join(list))
