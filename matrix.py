import random
n = 3
m = 3
matrix = []

for i in range(n):
    matrix.append([])
    for j in range(m):
        matrix[i]. append(random.randint(-9,9))

for i in range(n):
     print('')
     for j in range(m):
        print(matrix[i][j], end=' ')

for i in range(n):
    for j in range(m):
        if matrix[i][j] % 2 == 0 and matrix[i][j] != 0 :
            print('\nЧетные числа:', matrix[i][j])

zero = 0
for i in range(n):
    for j in range(m):
        if matrix[i][j] == 0:
            zero += 1

minus = 0
for i in range(n):
    for j in range(m):
        if matrix[i][j] <= 0:
            minus += 1

plus = 0
for i in range(n):
    for j in range(m):
        if matrix[i][j] >= 0:
            plus += 1

print(' ')
print('Количество нулей', zero)
print('Количество отрицательных:', minus)
print('Количество положительных:', plus)
