code
n = int(input())
moods = list(map(int, input().split()))

dp = [[False] * (n + 1) for _ in range(n + 1)]
dp[0][0] = True

for i in range(1, n + 1):
    for j in range(i + 1):
        if moods[j - 1]:
            p = 1
            while p * (n - 1) < i and p <= n:
                if i % p == 0:
                    dp[i][j] = True
                    break
                p += 1
        else:
            dp[i][j] = False

print("YES" if dp[n][n] else "NO")
