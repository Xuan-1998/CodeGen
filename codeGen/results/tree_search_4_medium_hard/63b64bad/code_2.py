def simulate_program(a):
    n = len(a) + 1
    dp = [-1] * (n - 1)
    prev = [[(1, 0)] for _ in range(n - 1)]

    for i in range(2, n):
        x, y = 1, 0
        for j in range(1, a[i]):
            if x <= 0 or x > i:
                dp[i - 1] = y
                break
            x, y = (x + a[x]) % i, y + a[x]
        else:
            dp[i - 1] = y

    return dp[-1]

a = list(map(int, input().split()))
print(simulate_program(a))
