a = int(input('\nВведите начальное число: '))
b = int(input('Введите последнее число: '))
list = list(range(a, b))
list_7 = []
p = 2
for i in list:
    if i % 7 == 0:
        list_7.append(i)
for i in list:
    if i == 1:
        list.remove(i)
list_1 = list
while p < list_1[-1]:
    for i in list_1:
        if i % p == 0 and p != i:
            list_1.remove(i)
    for i in list_1:
        if i > p:
            p = i
            break
print('\nВсе простые числа от ' + str(a) + ' до ' + str(b) + ': ' + ', '.join(map(str, list_1)) + '.')
print('\nВсе числа от ' + str(a) + ' до ' + str(b) + ' кратные 7: ' + ', '.join(map(str, list_7)) + '.')
