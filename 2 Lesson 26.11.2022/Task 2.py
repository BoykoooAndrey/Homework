# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
n = int(input("Введите число N:"))
list = []
for i in range(n+1):
    if i == 0:
        continue
    if i == 1:
        list.append(1)
    else:
        list.append(i*list[i-2])
print(list)