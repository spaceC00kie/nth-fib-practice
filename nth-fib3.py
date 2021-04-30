# given a number, return its value in the fibonacci sequence

def nth_fib(n, memo={1: 0, 2: 1}):
    if n in memo:
        return memo[n]
    memo[n] = nth_fib(n - 1, memo) + nth_fib(n - 2, memo)
    return memo[n]


print(nth_fib(12))

