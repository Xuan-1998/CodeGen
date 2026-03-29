def min_f(a, s):
    memo = {}

    def dp(n, k):
        if (n, k) in memo:
            return memo[(n, k)]

        if n == 0:
            return 0

        if n % 2 == 1:  # a_n is even
            y = a[n - 1]
            x = 0
        else:  # a_n is odd
            x = a[n - 1]
            y = 0

        f = dp(n - 1, k)
        if (x - k) * (y - k) >= 0:
            f += x * y
        return f

    min_val = float('inf')
    for i in range(len(a)):
        min_val = min(min_val, dp(i + 2, s))
    return min_val


t = int(input())
for _ in range(t):
    n, s = map(int, input().split())
    a = list(map(int, input().split()))
    print(min_f(a, s))
