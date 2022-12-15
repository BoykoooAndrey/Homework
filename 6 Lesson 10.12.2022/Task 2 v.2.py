# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных индексах. Индексы вводятся одной строкой, через пробел.
# n = 3
# [-3, -2, -1, 0, 1, 2, 3]
# --> 0 2 3
# -3 * -1 * 0 = 0
# Вывод: 0

n = int(input("Введите число N:"))
list = [i for i in range(-n, n+1)]
print(list)
b = str(input("Введите индексы через пробел:"))
c = b.split(' ')
multiplication = 1
for i in range(len(c)):
    multiplication *= list[int(c[i])]
print(multiplication)
