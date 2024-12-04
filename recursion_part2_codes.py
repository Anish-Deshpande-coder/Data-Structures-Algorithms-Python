def power(a, n): 
    if(n == 1):
        return a
    else:
        rest = power(a, n - 1)
        return a * rest




def fast_power2(a, n):

    if (n == 1):
        return a
    else:
        part1 = fast_power2(a, n // 2)
        part2 = fast_power1(a, n // 2)
        if (n % 2 == 0):
            return part1 * part1
        else: # n is odd
            return a * part1 * part1





def fast_power2(a, n):
    if (n == 1):
        return a
    else:
        part1 = fast_power1(a, n // 2)

        if (n % 2 == 0):
            return part1 * part1
        else: # n is odd
            return a * part1 * part1





def fib(n): #recursive fibnonacci number, runtime is exponential, Big-O(golden_ratio**n).
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        prev = fib(n-1)
        pre_prev = fib(n-2)
        return prev + pre_prev

# golden ratio is 1.61803398875 (phi = (1+sqrt(5))/2))
