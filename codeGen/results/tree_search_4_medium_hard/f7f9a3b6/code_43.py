def solve():
    n = int(input())
    s = input()
    a = [int(x) for x in input().split()]

    dp = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for k in range(i + 1):
            if all(s[j] != s[i - j - 1] or j > a[ord(s[i - j - 1]).lower() - ord('a')] for j in range(min(k, i))):
                dp[i][k] = (dp[i - 1][k - 1] + k + 1 if k > 0 else 1)
            else:
                dp[i][k] = dp[i - a[ord(s[i - 1]).lower() - ord('a')]][min(k, i)]

    print((sum(dp[n][k] for k in range(n + 1))) % (10**9 + 7))
    print(max(dp[n]))
    print(min(k for k in range(n + 1) if dp[n][k]))

if __name__ == "__main__":
    solve()
