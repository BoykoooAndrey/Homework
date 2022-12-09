a = "Я неабв люблю любабвлю Пайтонабв Питон"
list = a.split(' ')
list2 = []
for i in range(len(list)):
    if not ('абв' in list[i]):
        list2.append(list[i])
print(' '.join(list2))
