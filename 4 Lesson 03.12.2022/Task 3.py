# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся
# элементов исходной последовательности.
# Ввод: [1, 1, 2, 3, 4, 4, 4]
# Вывод: [2, 3]
nums = [1, 1, 2, 3, 4, 4, 4]
unique_nums = []
for i in range(len(nums)):
    count = 0
    for j in range(len(nums)):
        if nums[i] == nums[j]:
            count += 1
    if count == 1:
        unique_nums.append(nums[i])
print(unique_nums)
