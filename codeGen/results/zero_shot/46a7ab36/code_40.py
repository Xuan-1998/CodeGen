def alien_language_words(n, m):
    MOD = 10**8 + 7

    # Base case: empty string
    if m == 0:
        return 1

    # Recurrence relation
    dp = [0] * (m + 1)
    dp[0] = 1

    for i in range(1, m + 1):
        if 2 * i > n:
            dp[i] = dp[i - 1] * 2 % MOD
        else:
            dp[i] = dp[i - 1]

    return dp[m]

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    print(alien_language_words(n, m))
