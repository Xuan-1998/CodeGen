n = int(input())
a = list(map(int, input().split()))
dp = [0] * n

for i in range(n):
    if i == 0:
        dp[i] = n
    elif i == 1:
        dp[i] = n - (1 if a[0] == a[1] else 0)
    else:
        dp[i] = 1 + min(dp[j] for j in range(max(0, i-2), min(n, i+2))) if a[i] == a[k+1] or a[i] == a[k-1] else n

print(max(dp))
