# given a number, return its value in the fibonacci sequence

def nth_fib(n):
    prev = [0, 1]
    if n < 3:
        return prev[n - 1]
    count = 3
    while count <= n:
        prev[0], prev[1] = prev[1], prev[0] + prev[1]
        count += 1
        print(prev[1])
    return prev[1]


print(nth_fib(10000))
