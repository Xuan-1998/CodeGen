def min_operations(n, x):
    dp = [float('inf')] * (n + 1)
    dp[0] = 0

    for i in range(1, n + 1):
        for j in range(10):
            if len(str(x)) == i:
                return 0
            for k in range(1, 10):
                new_x = x * k
                if str(new_x).endswith(str(j)):
                    dp[i] = min(dp[i], dp[i - 1] + 1)

    return -1

n, x = map(int, input().split())
print(min_operations(n, x))
