from random import randint
n = 5 
m = 5 

a = []

for i in range(n):
    a.append([])
    for j in range(m):
        a[i].append(randint(-5, 5))
for i in range(n):
    print("")
    for j in range(m):
        print(a[i][j], end=' ')


b = 0
for i in range(n):
    for j in range(m):
        if a[i][j] > 0:
            b += 1

c = 0
for i in range(n):
    for j in range(m):
        if a[i][j] < 0:
            c += 1


print('\n')
print('Колл положительных', b)
print('Колл отрицательных', c)

