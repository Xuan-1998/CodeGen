def simulate_program(n, a):
    dp = [-1] * (n + 1)
    dp[0] = 0

    for i in range(2, n + 1):
        x = i
        y = dp[i - 1]
        while x > 0:
            if a[x - 1] <= x:
                x -= a[x - 1]
            else:
                y += a[x - 1]
                x = 0
            if dp[x] != -1:
                break
        dp[x] = y

    return [dp[i] for i in range(2, n + 1)]

n = int(input())
a = list(map(int, input().split()))
print(*simulate_program(n, a), sep="\n")
