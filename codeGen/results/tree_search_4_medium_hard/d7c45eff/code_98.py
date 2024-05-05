import sys

def solve():
    n, k = map(int, input().split())
    s = input()

    dp = [False] * (k + 1)
    dp[0] = True

    for i in range(1, k + 1):
        if s[i - 1] <= s[0]:
            dp[i] = dp[i - 1]
        else:
            dp[i] = dp[i - 1] or dp[i - 2]

    if not dp[k]:
        i = k
        while i > 0 and s[i - 1] != s[0]:
            i -= 1
        print(s[:i + 1])
    else:
        print(s)

if __name__ == "__main__":
    solve()
