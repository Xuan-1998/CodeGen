def min_function_value(a):
    n = len(a)
    s = int(1e9)  # initialize s to a large value

    for x in range(n):  # iterate over all possible values of x
        y = a[x] - x  # calculate corresponding value of y
        if (x - s) * (y - s) >= 0:  # check the condition (x - s) * (y - s) >= 0
            f = sum(i * j for i, j in zip(x, [a[x + 1] - x for x in range(n - 1)]))
            if f < s:
                s = f

    return s

t = int(input())
for _ in range(t):
    n, s = map(int, input().split())
    a = list(map(int, input().split()))
    print(min_function_value(a))
