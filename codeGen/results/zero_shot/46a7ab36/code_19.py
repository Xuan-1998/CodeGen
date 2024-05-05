def calc_possible_letters(n, m):
    dp = [[0] * (m + 1) for _ in range(n)]
    for i in range(1, n + 1):
        if 2 * i > n:
            dp[i][0] = n
        else:
            dp[i][0] = 1
    for j in range(1, m + 1):
        for i in range(1, n + 1):
            if 2 * i <= n:
                dp[i][j] = 1
            else:
                dp[i][j] = n
    return [dp[i][m] for i in range(1, n + 1)]

def total_possible_words(n, m):
    possibilities = calc_possible_letters(n, m)
    return sum((pow(10, i) + 7) * p for i, p in enumerate(reversed(possibilities)))

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    print(total_possible_words(n, m))
