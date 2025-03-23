def f(n):
    c = 0
    while n >= 0:
        n = n-2
        c = c + n - 2
    return c

for i in range(50):
    print(i, f(i))