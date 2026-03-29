def solve(n, s, a):
    MOD = 10**9 + 7

    dp = [[0]*(n+1) for _ in range(n+1)]

    for i in range(1, n+1):
        c = set(s[:i])
        for k in range(i):
            if all(s[j] != s[k] or a[ord(s[k])-97] == 0 for j in range(k+1, i)):
                dp[i][k+1] += (dp[k][0] + sum(1 if c & (1 << ord(c)-97) and a[ord(c)-97] > 0 else 0 for c in c))
        dp[i][i] = 1

    ans1 = sum(dp[n][k] for k in range(n+1)) % MOD
    ans2 = max(k for k in range(1, n+1) if dp[n][k]) % MOD
    ans3 = min(k for k in range(1, n+1) if dp[n][k]) % MOD

    return [str(ans1), str(ans2), str(ans3)]


n = int(input())
s = input()
a = list(map(int, input().split()))

print(*solve(n, s, a))
