def min_f(n, s, a_n):
    memo = {}

    def f():
        if (n, s, a_n) in memo:
            return memo[(n, s, a_n)]

        if n == 0:
            return a_n

        min_val = float('inf')
        for x_i in range(s + 1):
            y_i = a_n - x_i
            if (x_i - s) * (y_i - s) >= 0:
                val = x_i * f(1, s, y_i) + y_i * f(1, s, x_i)
                min_val = min(min_val, val)

        memo[(n, s, a_n)] = min_val
        return min_val

    return f()(0, s, n)

t = int(input())
for _ in range(t):
    n, s = map(int, input().split())
    print(min_f(n, s, sum(map(int, input().split()))))
