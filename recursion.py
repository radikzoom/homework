def a(n):
    if n <= 0:
        return 1
    else:
        return a(n // 2) +a(n // 3)

for i in range(0, 10):
    print(a(i), end=' ')

print(' ')

def a(n):
    if n <= 1:
        return 1
    else:
        return n - a(a(n-1))

for i in range(0, 10):
    print(a(i), end=' ')
