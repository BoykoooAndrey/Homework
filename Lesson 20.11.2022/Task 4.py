# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).
plane = int(input('Введите номер плоскости:'))
if plane == 1:
    print('Диапазон x и y  в плоскости: x(0, +∞), y(0, +∞)')
elif plane == 2:
    print('Диапазон x и y  в плоскости: x(-∞, 0), y(0, +∞)')
elif plane == 3:
    print('Диапазон x и y  в плоскости: x(-∞, 0), y(-∞, 0)')
elif plane == 4:
    print('Диапазон x и y  в плоскости: x(0, +∞), y(-∞, 0)')
else:
    print(f'Плоскости под номером {plane} нет')
