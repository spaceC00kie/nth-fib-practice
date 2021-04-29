# given a number, return its value in the fib sequence

def nth_fib(n):
    # if 1 return 0
    if n == 1:
        return 0
    # if 2 return 1
    if n == 2:
        return 1

    # otherwise sum fib n-1 and n-2
    return nth_fib(n - 1) + nth_fib(n - 2)


print(nth_fib(100))

