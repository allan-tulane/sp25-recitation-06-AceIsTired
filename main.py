def fib_recursive(n, counts):
    if n == 0:
        counts[0] += 1
        return 0
    elif n == 1:
        counts[1] += 1
        return 1
    else:
        counts[n] += 1
        recursive_result = fib_recursive(n - 1, counts) + fib_recursive(n - 2, counts)
        return recursive_result



def fib_top_down(n, fibs):
    if n == 0:
        fibs[0] = 0
        return 0
    elif n == 1:
        fibs[1] = 1
        return 1

    if fibs[n] != -1:
        return fibs[n]

    fibs[n] = fib_top_down(n - 1, fibs) + fib_top_down(n - 2, fibs)
    return fibs[n]


def fib_bottom_up(n):
    fibs = [0] * (n + 1)
    if n >= 1:
        fibs[1] = 1

    for i in range(2, n + 1):
        fibs[i] = fibs[i - 1] + fibs[i - 2]

    return fibs[n]




