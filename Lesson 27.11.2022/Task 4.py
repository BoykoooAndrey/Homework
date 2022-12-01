# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

def fib(n):
    if n == 0:
        return 0
    if n < 0:
        if n in [-1]:
            return 1
        else:
            return fib(n+2) - fib(n+1)
    if n > 0:
        if n in [1]:
            return 1
        else:
            return fib(n-1) + fib(n-2)

def row_fib(n, list):
    for i in range(-n, n+1):
        list.append(fib(i))
    return list

n = 8
list = []
row = row_fib(n, list)
print(row)
