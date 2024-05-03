===BEGIN CODE===
n = int(input())
arr = list(map(int, input().split()))
dp = [False] * (n + 1)
dp[0] = True

for i in range(1, n + 1):
    if dp[i - 1]:
        if arr[i - 1] >= 1:
            dp[i] = True
        else:
            dp[i] = dp[i - 1]
    else:
        dp[i] = False

print("YES" if dp[n] else "NO")
===END CODE===
