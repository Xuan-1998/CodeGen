import sys

def solve():
    N = int(input())
    str1 = input().strip()
    str2 = input().strip()

    lcp = [0] * (N + 1)
    for i in range(N):
        for j in range(i, -1, -1):
            if str1[j] == str2[i - j]:
                lcp[i + 1] = lcp[i] + 1
            else:
                break

    dp = [[0] * (N + 1) for _ in range(N + 1)]
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if lcp[i - 1] == lcp[j - 1]:
                dp[i][j] = max(dp[i - 1][j - 1], lcp[i - 1])
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[-1][-1]

print(solve())
