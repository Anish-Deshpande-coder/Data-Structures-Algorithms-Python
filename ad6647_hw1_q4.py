def fibs(n):
    a, b = 1, 1
    for num in range(n):
        yield a
        a, b = b, a + b
