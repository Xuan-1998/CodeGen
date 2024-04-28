n = int(input())
a = list(map(int, input().split()))
dp = [0] * (n + 1)
for i in range(2, n):
    dp[i] = max(dp[i-1], a[i-1])
for i in range(n-1, -1, -1):
    if dp[i] > 0:
        j = i
        while j < n and (a[j] == a[i] or a[j] == a[i] + 1 or a[j] == a[i] - 1):
            j += 1
        if j != i:
            dp[i] -= 1
    else:
        break
print(max(dp))
