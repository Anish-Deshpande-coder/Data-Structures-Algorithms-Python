def reverse(x):
    flag = False
    if x < 0:
        flag = True
        x = 0 - x
    result = 0
    while (x > 0):
        result = result * 10 + (x % 10)
        x = x // 10

    if (flag == True):
        result = 0 - result

    return result

print(reverse(123))
