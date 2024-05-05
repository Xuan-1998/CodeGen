def count_possible_words(n, m):
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(1, n + 1):
        if 2 * i > n:
            for j in range(m):
                dp[j % n + 1] += dp[j]
        else:
            for j in range(m - 1):
                dp[(j + 1) % (n // 2) + 1] += dp[j]
    return sum(dp[:m]) % (10**8 + 7)

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    print(count_possible_words(n, m))
