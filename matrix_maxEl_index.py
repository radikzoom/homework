from random import randint

n = 3
m = 5
k = 7

t = []
for n1 in range(n):
    t.append([])
    for m1 in range(m):
        t[n1].append([])
        for k1 in range(k):
            t[n1][m1].append(randint(-20, 20))
#
for n1 in range(n): # обрати внимание как распечатал матрицу
    print(' ')
    for m1 in range(m):
        print(' ')
        for k1 in range(k):
            print(t[n1][m1][k1], end=' ')

max_el = -100
for n2 in range(n):
    for m2 in range(m):
        for k2 in range(k):
            if t[n2][m2][k2] > max_el:
                max_el = t[n2][m2][k2]
ind_x = []
for n3 in range(n):
    ind_x.append([])
    for m3 in range(m):
        ind_x[n3].append([])
        for k3 in range(k):
            if t[n3][m3][k3] == max_el:
                print('\nИндекс макс.значений матрицы:', n3, m3, k3)

print(max_el)



