# Распаковка

output = 'output.txt'
unpacked = 'unpacked.txt'


with open(output, 'r') as f:
    temp_list1 = f.read().split(' ')
    with open(unpacked, 'a') as f:
        for i in range(0, len(temp_list1), 2):
            f.writelines(int(temp_list1[i]) * temp_list1[i+1])
