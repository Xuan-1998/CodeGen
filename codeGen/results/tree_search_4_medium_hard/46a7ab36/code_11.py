import sys

def count_words(n, m):
    dp = {0: 1}  # base case: a word with no letters is possible
    for k in range(1, n + 1):
        if 2 * k > n:
            dp[k] = (n - k + 1) * dp[k - 1]
        else:
            dp[k] = sum(dp.get(min(n, 2 * i), 0) for i in range(k))
    return pow(10, 8) + 7, dp[m]

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    words, dp = count_words(n, m)
    print(words % (pow(10, 9) + 7))
