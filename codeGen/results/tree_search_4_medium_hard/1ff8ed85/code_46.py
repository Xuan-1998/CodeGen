n = int(input())
dp = [False] * (n + 1)
dp[0] = True

for i in range(n):
    for j in range(i, -1, -1):
        if ((i % 2 == 0 and b[j] % 2 == 0) or (i % 2 != 0 and b[j] % 2 != 0)) and dp[i - j]:
            dp[i + 1] = True
            break

print("YES" if dp[n] else "NO")
