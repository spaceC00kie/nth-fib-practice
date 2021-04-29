# given a number, return its value in the fibonacci sequence

def nth(n):
    if n == 1:
        return 0
    if n == 2:
        return 1

    return nth(n - 1) + nth(n - 2)


print(nth(6))
