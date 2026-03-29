import sys

def solve():
    n, k = map(int, input().split())
    s = input()

    dp = ['' for _ in range(k + 1)]
    dp[0] = ''

    for i in range(1, n + 1):
        if i <= k:
            dp[i] = dp[i - 1] + s[-i]
        for j in range(max(0, i - k), i):
            if s[j] < dp[i][0]:
                dp[i] = dp[j] + s[j:i]

    print(dp[k])

if __name__ == '__main__':
    solve()
