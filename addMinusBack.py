from random import randint
a = [randint(-20,20) for i in range(20)]

sumZero = 0                     # summ zero element
for i in a:
    if i == 0:
        sumZero += 1


stringA = []
for i in range (len(a)):
    if a[i] > 0:
        stringA.append(a[i])
for i in range (sumZero):
    stringA.append(0)
for i in range (len(a)):
    if a[i] < 0:
        stringA.append(a[i])

print(a)
print(stringA)
