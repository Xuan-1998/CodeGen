n, m = map(int, input().split())
arr = list(map(int, input().split()))

dp = [False] * (n + 1)
dp[0] = True

for i in range(1, n + 1):
    for j in range(i):
        if arr[j] <= arr[i]:
            dp[i] = max(dp.get(j, 0), dp[i])
        else:
            break

for _ in range(m):
    l, r = map(int, input().split())
    print("Yes" if dp[r] and not dp[l - 1] else "No")
