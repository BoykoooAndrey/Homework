# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
def multipliers(val):
    for i in range(2, val):
        if val % i == 0:
            list.append(int(i))
            val /= i
        elif val == 2:
            list.append(int(2))
            return
        elif val == i:
            list.append(int(val))
            return


val = int(input("Введите число:"))
list = []


multipliers(val)
print(list)
